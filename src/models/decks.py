from .deck import Deck
from .card import Card
from .database import Database
from .observable_model import Event


class Decks(Event, list):
    def __init__(self, database: Database):
        super().__init__()
        self.database = database
        decks = self.database.get_decks()

        self.decks = []

        for deck in decks:
            deck = Deck(iid=deck["id"], name=deck["name"])
            deck.add_event_listener("ADD_CARD", fn=self.add_card_handler)
            deck.add_event_listener("DELETE_CARD", fn=self.delete_card_handler)
            self.decks.append(deck)

        self.cards = self.database.get_cards()

        for deck in self.decks:
            deck.cards = list(filter(lambda c: c.iid == deck.iid, self.cards))

    def __setitem__(self, index, item):
        super().__setitem__(index, item)

    def insert(self, index, item):
        super().insert(index, item)

    def append(self, item):
        self.decks.append(item)
        self.notify("ADD_DECK", item)

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(item for item in other)

    def get_deck_by_iid(self, iid):
        for deck in self.decks:
            if deck.iid == str(iid):
                return deck
        return None

    def remove_deck(self, iid):
        deck = self.get_deck_by_iid(iid)
        if not deck:
            raise ValueError
        self.decks.remove(deck)
        self.database.delete_deck(iid)
        self.notify("DELETE_DECK", deck)

    def add_card_handler(self, data):
        self.notify("UPDATE_DECK", data)

    def delete_card_handler(self, data):
        self.notify("UPDATE_DECK", data)

    def create_deck(self, deck_name: str):
        deck = self.database.create_deck(deck_name)
        deck.add_event_listener("ADD_CARD", fn=self.add_card_handler)
        deck.add_event_listener("DELETE_CARD", fn=self.delete_card_handler)
        self.append(deck)
        return deck
