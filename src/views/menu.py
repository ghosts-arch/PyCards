from tkinter import messagebox
from tkinter.ttk import Button, Frame, Treeview, Label

from .view import View


from ..components.decks_treeview import DecksTreeview

from ..play_cards_windows import PlayCardsWindow


class Menu(View):
    def __init__(self, container, app):
        super().__init__(container, app)
        self.container = container
        self.app = app

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        frame = Frame(self)

        title = Label(frame, text="Vos decks", font=("Lato", 24, "bold"))
        title.grid(row=0, padx=8, pady=8)

        columns = ["name", "cards_count"]

        self.treeview = DecksTreeview(frame, columns=columns, decks=self.app.decks)
        self.app.events.attach("menu_decks_treeview", self.treeview)

        self.treeview.grid(row=1, padx=8, pady=8)

        self.add_deck_button = Button(frame, text="Ajouter un deck")
        self.add_deck_button.grid(row=2, padx=8, pady=8)
        frame.grid(row=0, padx=8, pady=8)
