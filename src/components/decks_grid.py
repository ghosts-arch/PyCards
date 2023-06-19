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

    def update(self, message_type, subject):
        match message_type:
            case "ADD_DECK":
                self._d[subject.iid] = DeckCard(self, self._app, deck=subject)
                self._d[subject.iid].grid(
                    row=int(len(self._d) / 3),
                    column=len(self._d) % 3,
                    padx=8,
                    pady=8,
                )

            case "DELETE_DECK":
                self._d[subject].grid_forget()
                self._d.pop(subject)

        """
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
        """
