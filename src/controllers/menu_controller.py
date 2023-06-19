from .editor_controller import EditorController
from ..views.editor import Editor
from ..play_cards_windows import PlayCardsWindow
from ..models.model import Model
from ..views.view import View


class MenuController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["Home"]
        self._bind()
        self.load_decks()

    def load_decks(self):
        for deck in self.model.decks._decks:
            self.add_deck(deck=deck)

    def _bind(self):
        self.frame.add_deck_button.config(command=self.create_deck)

    def create_deck(self):
        self.view.frames["Editor"] = Editor(self.view._root)
        self.editor_controller = EditorController(self.model, view=self.view, deck=None)
        self.view.to("Editor")

    def add_deck(self, deck):
        card = self.frame.decks_grid.create_card(deck)
        card.bind(
            sequence="<Double-Button-1>",
            func=lambda e: card.deck_card_menu.tk_popup(e.x_root, e.y_root),
        )
        card.deck_card_menu.add_command(
            label="Editer", command=lambda: self.edit_deck(deck)
        )
        card.play_button.configure(command=self.start_deck)

    def edit_deck(self, deck):
        self.view.frames["Editor"] = Editor(self.view._root)
        self.editor_controller = EditorController(self.model, view=self.view, deck=deck)
        self.view.to("Editor")

    def start_deck(self):
        PlayCardsWindow(self, [])
