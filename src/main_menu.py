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
        self.treeview.grid(row=1, padx=8, pady=8)

        frame.grid(row=0, padx=8, pady=8)

        start_btn = Button(self, text="Demarrer", command=self.show_play_cards_window)

        # start_btn.grid(row=1, padx=8, pady=8)

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
