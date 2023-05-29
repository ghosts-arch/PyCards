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

        self.treeview = Treeview(frame, columns=("name"), show="", selectmode="browse")

        for deck in container.master.decks:
            self.insert_item(deck)

        self.treeview.bind("<<TreeviewSelect>>", self._item_selected)

        self.treeview.grid(row=1, padx=8, pady=8)

        frame.grid(row=0, padx=8, pady=8)

        start_btn = Button(
            frame, text="Ajouter un deck", command=self.show_play_cards_window
        )

        start_btn.grid(
            row=2,
            padx=8,
            pady=8,
            sticky="news",
        )

    def insert_item(self, card):
        self.treeview.insert(
            "",
            "end",
            values=[card["name"]],
            iid=card["id"],
        )

    def show_play_cards_window(self):
        if not len(self.container.master.cards):
            return messagebox.showerror("Erreur", "Aucune carte trouvée !")
        PlayCardsWindow(self)

    def _item_selected(self, event):
        for selected_item in self.treeview.selection():
            decks_cards = list(
                filter(
                    lambda card: card["deck_id"] == selected_item,
                    self.container.master.cards,
                )
            )
            print(decks_cards)
            if not len(decks_cards):
                return messagebox.showerror("Erreur", "Empty deck")
            item = self.treeview.item(selected_item)
            PlayCardsWindow(self)
