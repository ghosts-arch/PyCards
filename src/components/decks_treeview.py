from tkinter import messagebox
from tkinter.ttk import Treeview
from ..core.deck import Deck

from ..play_cards_windows import PlayCardsWindow


class DecksTreeview(Treeview):
    def __init__(self, master, columns, decks: list[Deck]) -> None:
        print(decks)
        super().__init__(master=master, columns=columns, show="", selectmode="browse")
        self._decks = decks
        for column in columns:
            self.column(column=column, anchor="center")

        for deck in self._decks:
            self.insert_item(deck)

        self.bind("<<TreeviewSelect>>", self._item_selected)

    def insert_item(self, deck: Deck):
        self.insert(
            "",
            "end",
            values=[f"{deck.name}", f"{len(deck.cards)} cartes"],
            iid=deck.iid,
        )

    def _item_selected(self, event):
        for selected_item in self.selection():
            decks_cards = list(
                filter(lambda deck: deck == int(selected_item), self._decks)
            )
            if not len(decks_cards):
                return messagebox.showerror("Erreur", "Empty deck")
            PlayCardsWindow(self, decks_cards)

    def update(self, subject):
        print(f"update decks treeview - ", subject)
        self.insert_item(subject)
