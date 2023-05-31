from tkinter import messagebox
from tkinter.ttk import Button, Frame, Treeview, Label

from .play_cards_windows import PlayCardsWindow


class MainMenu(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        frame = Frame(self)

        title = Label(frame, text="Vos decks", font=("Lato", 24, "bold"))
        title.grid(row=0, padx=8, pady=8)

        columns = ["name", "cards_count"]
        self.treeview = Treeview(frame, columns=columns, show="", selectmode="browse")
        for column in columns:
            self.treeview.column(column=column, anchor="center")

        for deck in container.master.decks:
            self.insert_item(deck)

        self.treeview.bind("<<TreeviewSelect>>", self._item_selected)

        self.treeview.grid(row=1, padx=8, pady=8)

        frame.grid(row=0, padx=8, pady=8)

        start_btn = Button(frame, text="Ajouter un deck")

        start_btn.grid(
            row=2,
            padx=8,
            pady=8,
        )

    def insert_item(self, deck):
        self.treeview.insert(
            "",
            "end",
            values=[f'{deck["name"]}', f'{deck["cards_count"]} cartes'],
            iid=deck["id"],
        )

    def _item_selected(self, event):
        for selected_item in self.treeview.selection():
            decks_cards = list(
                filter(
                    lambda card: card["deck_id"] == int(selected_item),
                    self.container.master.cards,
                )
            )
            print(decks_cards)
            if not len(decks_cards):
                return messagebox.showerror("Erreur", "Empty deck")
            PlayCardsWindow(self, decks_cards)
