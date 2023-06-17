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
        pass

    def _bind(self):
        self.frame.add_deck_button.config(command=self.create_deck)

    def create_deck(self):
        self.view.to("Editor")

    def add_deck(self, deck):
        self.frame.decks_grid.add_deck(deck)
