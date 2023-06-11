# https://realpython.com/inherit-python-list/


class DecksList(list):
    def __init__(self, iterable):
        super().__init__(item for item in iterable)
        self._decks = iterable

    def __setitem__(self, index, item):
        super().__setitem__(index, item)

    def insert(self, index, item):
        super().insert(index, item)

    def append(self, item):
        self._decks.append(item)

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
