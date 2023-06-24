from tkinter import ttk
import tkinter

from ..play_cards_windows import PlayCardsWindow


class DeckCard(ttk.Frame):
    def __init__(self, container, app, deck):
        self._app = app
        self._deck = deck
        self._container = container
        super().__init__(container, relief="groove")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.deck_card_menu = tkinter.Menu(self, tearoff=False)

        self.deck_title = ttk.Label(
            self,
            text=f"{self._deck.name} - {len(self._deck.cards)} cartes",
            font=("Lato", 16, "bold"),
        )
        self.deck_title.grid(row=0, padx=8, pady=8)

        self.play_button = ttk.Button(self, text="Demarrer")
        self.play_button.grid(
            row=2,
            column=2,
            padx=8,
            pady=8,
            sticky="e",
        )

    def edit_deck_title(self, new_text):
        self.deck_title.config(text=new_text)
