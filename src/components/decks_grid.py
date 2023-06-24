from tkinter import ttk

from .deck_card import DeckCard


class DecksGrid(ttk.Frame):
    def __init__(self, container, app, no_content_message: str = ""):
        super().__init__(container, name="decks_grid")
        self._app = app
        self._container = container
        self.no_content_message = no_content_message

        self._d = {}

        if not self._d:
            self.no_content_label = ttk.Label(
                self, text=no_content_message, font=("Lato", 16, "italic")
            )
            self.no_content_label.grid(padx=8, pady=8)

    def create_card(self, deck):
        if len(self._d) + 1 > 9:
            return
        self._d[deck.iid] = DeckCard(self, self._app, deck=deck)
        if len(self._d) > 0:
            self.no_content_label.grid_forget()
        self._d[deck.iid].grid(
            row=int((len(self._d) - 1) / 3),
            column=(len(self._d) - 1) % 3,
            padx=8,
            pady=8,
        )
        return self._d[deck.iid]

    def delete_card(self, card):
        self._d[card.iid].grid_forget()
        self._d.pop(card.iid)
        if len(self._d) == 0:
            self.no_content_label.grid(padx=8, pady=8)

    def update_card(self, deck):
        self._d[deck.iid].edit_deck_title(
            new_text=f"{deck.name} - {len(deck.cards)} cartes"
        )
