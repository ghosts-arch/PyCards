from .editor_controller import EditorController
from ..models.model import Model
from .menu_controller import MenuController
from ..views.view import View


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.menu_controller = MenuController(model, view)

        self.model.decks.add_event_listener(event="ADD_DECK", fn=self.add_deck_handler)

    def add_deck_handler(self, data):
        self.menu_controller.add_deck(data)

    def start(self):
        self.view.to("Home")
        self.view.start_main_loop()
