from tkinter import Tk
from tkinter.ttk import Frame, Style

from .dark_theme import dark_theme
from .components.navbar import Navbar

from .database import Database
from .cards_management import CardsManagement
from .main_menu import MainMenu


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

        s = Style()
        s.theme_create("dark", parent="default", settings=dark_theme)
        s.theme_use("dark")

        self.main_section = Frame(self)

        self.frames = {}

        for F in (MainMenu, CardsManagement):
            page_name = F.__name__
            frame = F(container=self.main_section, app=self)
            self.frames[page_name] = frame
            frame.grid(row=1, sticky="news", columnspan=2)

        navbar = Navbar(self)
        navbar.grid(row=0)

        self.main_section.grid(row=1, sticky="news", columnspan=2)
        self.main_section.grid_columnconfigure(0, weight=1)

        self.to("MainMenu")

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

        frame.tkraise()
