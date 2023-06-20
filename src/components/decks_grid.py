from tkinter import ttk

from .deck_card import DeckCard


class DecksGrid(ttk.Frame):
    def __init__(self, container, app):
        super().__init__(container, name="decks_grid")
        self._app = app
        self._container = container

        self._d = {}

    def create_card(self, deck):
        self._d[str(deck.iid)] = DeckCard(self, self._app, deck=deck)
        self._d[deck.iid].grid(
            row=int(len(self._d) / 3), column=len(self._d) % 3, padx=8, pady=8
        )
        return self._d[str(deck.iid)]

    def delete_card(self, card):
        self._d[card.iid].grid_forget()
        self._d.pop(card.iid)

    def update_card(self, deck):
        self._d[str(deck.iid)].edit_deck_title(
            new_text=f"{deck.name} - {len(deck.cards)} cartes"
        )
