from ..observer import Subject


class Deck(Subject):
    def __init__(self, iid, name) -> None:
        super().__init__()
        self._iid = iid
        self._name = name
        self._cards = []

    @property
    def iid(self):
        return self._iid

    @property
    def name(self):
        return self._name

    @property
    def cards(self):
        return self._cards

    @name.setter
    def name(self, value):
        self._name = value
        self.notify()

    @cards.setter
    def cards(self, value):
        self._cards = value
