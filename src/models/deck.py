from .card import Card
from .observable_model import Event


class Deck(Event):
    def __init__(self, name, iid) -> None:
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

    @cards.setter
    def cards(self, value):
        self._cards = value

    def get_card_by_iid(self, iid):
        for card in self._cards:
            if card.iid == iid:
                return card

    def add_card(self, card: Card):
        self._cards.append(card)
        self.notify("ADD_CARD", (self, card))

    def remove_card(self, card: Card):
        self._cards.remove(card)
        self.notify("DELETE_CARD", (self, card))

    def update_card(self, old_card: Card, card: Card):
        self._cards[self._cards.index(old_card)] = card

    @name.setter
    def name(self, name):
        self._name = name
        self.notify("UPDATE_NAME", (self,))
