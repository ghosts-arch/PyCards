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

        deck_card_menu = tkinter.Menu(self, tearoff=False)
        deck_card_menu.add_command(label="Editer", command=self.edit_deck)

        self.bind(
            sequence="<Double-Button-1>",
            func=lambda e: deck_card_menu.tk_popup(e.x_root, e.y_root),
        )

        deck_title = ttk.Label(
            self,
            text=f"{self._deck.name} - {len(self._deck.cards)} cartes",
            font=("Lato", 16, "bold"),
        )
        deck_title.grid(row=0, padx=8, pady=8)

        play_button = ttk.Button(self, text="Demarrer", command=self.start_deck)
        play_button.grid(
            row=2,
            column=2,
            padx=8,
            pady=8,
            sticky="e",
        )

    def edit_deck(self):
        self._app.to_editor(self._deck)

    def start_deck(self):
        PlayCardsWindow(self, self._deck)
