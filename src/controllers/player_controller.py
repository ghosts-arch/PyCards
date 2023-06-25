from random import choice
from ..views.view import View
from ..models.model import Model


class PlayerController:
    def __init__(self, model: Model, view: View, deck) -> None:
        self.model = model
        self.view = view
        self.deck = deck
        self.frame = self.view.frames["Player"]
        self.current_card = self.generate_random_card()
        self.bind()
        self.display_card(self.current_card)

    def bind(self):
        self.frame.to_menu_button.config(command=self.back_to_home)

    def back_to_home(self):
        self.view.to("Home")

    def generate_random_card(self):
        return choice(self.deck.cards)

    def display_card(self, card):
        self.frame.question_txt.config(text=card.question)
