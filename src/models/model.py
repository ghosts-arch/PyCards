from .deck import Deck
from .decks import Decks


class Model:
    def __init__(self, database) -> None:
        self._decks = Decks(database=database)

    @property
    def decks(self):
        return self.decks
