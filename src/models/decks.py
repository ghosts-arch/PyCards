from ..database import Database
from .observable_model import Event


class Decks(Event, list):
    def __init__(self, database: Database):
        super().__init__()
        self._database = database
        self._decks = self._database.get_decks()
        self.cards = self._database.get_cards()

        for deck in self._decks:
            deck.cards = list(filter(lambda c: c.iid == deck.iid, self.cards))

    def __setitem__(self, index, item):
        super().__setitem__(index, item)

    def insert(self, index, item):
        super().insert(index, item)

    def append(self, item):
        self._decks.append(item)
        self.notify("ADD_DECK", item)

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(item for item in other)

    def get_deck_by_iid(self, iid):
        for deck in self._decks:
            if deck.iid == iid:
                return deck

    def remove_deck(self, iid):
        deck = self.get_deck_by_iid(iid)
        self._decks.remove(deck)

    def create_deck(self, deck_name: str):
        deck = self._database.create_deck(deck_name)
        self.append(deck)
        return deck
