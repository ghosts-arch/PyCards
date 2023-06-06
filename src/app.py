from tkinter import Tk
from tkinter.ttk import Frame, Style, Notebook

from .components.navbar import Navbar

from .database import Database
from .cards_management import CardsManagement
from .main_menu import MainMenu

dark_theme = {
    ".": {
        "configure": {"background": "#2d2d2d", "foreground": "white", "font": "Lato"}
    },
    "TButton": {
        "configure": {
            "background": "blue",
            "padding": [8, 8, 8, 8],
            "borderwidth": 0,
            "relief": "flat",
        },
        "map": {
            "background": [("active", "darkblue"), ("disabled", "grey")],
        },
    },
    "TEntry": {"configure": {"fieldbackground": "#4d4d4d"}},
    "Danger.TButton": {
        "configure": {"background": "red"},
        "map": {
            "background": [
                ("active", "darkred"),
            ],
        },
    },
    "Success.TButton": {
        "configure": {"background": "green"},
        "map": {
            "background": [
                ("active", "darkgreen"),
            ],
        },
    },
    "Navbar.TFrame": {"configure": {"background": "#2d2d2d"}},
    "Default.TButton": {
        "configure": {"background": "grey"},
        "map": {
            "background": [("active", "darkgrey")],
        },
    },
    "TNotebook.Tab": {"map": {"background": [("selected", "blue")]}},
    "Treeview": {
        "configure": {
            "font": ("Lato", 16, "normal"),
            "padding": [8, 8, 8, 8],
            "background": "#2d2d2d",
            "rowheight": 32,
            "borderwidth": 0,
            "anchor": "w",
            "fieldbackground": "#2d2d2d",
        },
        "map": {"background": [("selected", "#6d6d6d")]},
    },
    "Treeview.treearea": {"configure": {"foreground": "red"}},
    "TSeparator": {"configure": {"background": "##4d4d4d"}},
    "TCombobox": {
        "configure": {
            "background": "#2d2d2d",  # Dark grey background
            "foreground": "white",  # White text
            "fieldbackground": "#4d4d4d",
            "insertcolor": "white",
            "bordercolor": "black",
            "lightcolor": "#4d4d4d",
            "darkcolor": "black",
            "arrowcolor": "white",
        },
    },
}


class App(Tk):
    def __init__(self):
        super().__init__()
        self.database = Database()
        self.database.connect()
        self.database.init()

        self.decks = self.database.get_decks()
        self.cards = self.database.get_cards()

        for deck in self.decks:
            deck["cards"] = list(
                filter(lambda c: c["deck_id"] == deck["id"], self.cards)
            )

        self.title("PyCards")
        self.state("zoomed")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # styles

        s = Style()
        s.theme_create("dark", parent="default", settings=dark_theme)
        s.theme_use("dark")

        s.configure(
            "TButton",
            font=("Lato", 12),
        )
        s.configure("TLabel", font=("Lato", 12))
        s.configure(
            "Treeview.Heading",
            font=("Lato", 12),
            padding=[8, 8, 8, 8],
            borderwidth=0,
            background="#4d4d4d",
        )
        s.configure(
            "TNotebook.Tab",
            font=("Lato", 12),
            padding=[8, 8, 8, 8],
            borderwidth=0,
        )
        s.configure(
            "TNotebook",
            tabposition="n",
            font=("Lato", 65),
            tabmargins=[8, 8, 8, 8],
            borderwidth=0,
            relief="solid",
        )
        s.configure("Default.TButton", background="grey")
        # s.configure("Success.TButton", background="green")

        self.main_section = Frame()
        self.main_section.grid(row=1, sticky="news", columnspan=2)

        self.frames = {}

        for F in (MainMenu, CardsManagement):
            page_name = F.__name__
            frame = F(container=self.main_section, app=self)
            self.frames[page_name] = frame

        print(self.frames)

        navbar = Navbar(self)
        navbar.grid(row=0)

    def get_deck_by_id(self, iid: str):
        for deck in self.decks:
            if deck["id"] == int(iid):
                return deck

    def _get_deck_by_id(self, iid: str):
        for i, deck in enumerate(self.decks):
            if deck["id"] == int(iid):
                return i

    def _get_card_by_iid(self, iid: str):
        for index, card in enumerate(self.cards):
            if card["id"] == int(iid):
                return index
        return None

    def remove_card(self, iid: str):
        card = self._get_card_by_iid(iid)
        return self.cards.pop(card)  # type: ignore

    def remove_deck(self, iid):
        deck = self._get_deck_by_id(iid)
        return self.decks.pop(deck)  # type: ignore

    def to(self, frame_id):
        frame = self.frames[frame_id]
        # frame.reset()
        frame.tkraise()
