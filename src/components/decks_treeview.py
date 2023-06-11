from tkinter import messagebox
from tkinter.ttk import Treeview
from ..core.deck import Deck

from ..play_cards_windows import PlayCardsWindow


class DecksTreeview(Treeview):
    def __init__(self, master, columns, decks: list[Deck]) -> None:
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
            deck = self._decks.get_deck_by_iid(selected_item)
            if not len(deck.cards):
                return messagebox.showerror("Erreur", "Empty deck")
            PlayCardsWindow(self, deck)

    def update(self, message_type, subject):
        match message_type:
            case "ADD_DECK":
                self.insert_item(subject)
            case "DELETE_DECK":
                self.delete(f"{subject}")
            case "ADD_CARD":
                self.item(
                    f"{subject.iid}",
                    values=[f"{subject.name}", f"{len(subject.cards)} cartes"],
                )
            case "DELETE_CARD":
                self.item(
                    f"{subject.iid}",
                    values=[f"{subject.name}", f"{len(subject.cards)} cartes"],
                )
