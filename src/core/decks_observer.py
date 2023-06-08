from ..core.deck import Deck
from ..observer import Subject


class Decks(Subject):
    def __init__(self, decks: list[Deck] = []) -> None:
        super().__init__()
        self._decks = decks

    def add_deck(self, deck: Deck):
        self.notify(deck)
        self._decks.append(deck)

    def remove_deck(self, deck: Deck):
        self._decks.remove(deck)
