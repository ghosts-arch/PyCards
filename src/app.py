from tkinter import Tk
from tkinter.ttk import Frame, Style

from .events import Event

from .core.decks_observer import Decks

from .core.deck import Deck

from .themes.dark_theme import dark_theme
from .navbar import Navbar

from .database import Database
from .decks_list import CardsManagement
from .menu import Menu


class App(Tk):
    def __init__(self):
        super().__init__()
        self.database = Database()
        self.database.connect()
        self.database.init()

        self.decks = self.database.get_decks()
        self.cards = self.database.get_cards()

        for deck in self.decks:
            deck.cards = list(filter(lambda c: c.iid == deck.iid, self.cards))

        self.events = Event()

        self.title("PyCards")
        self.state("zoomed")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        s = Style()
        s.theme_create("dark", parent="default", settings=dark_theme)
        s.theme_use("dark")

        self.main_section = Frame(self)

        self.frames = {}

        for F in (Menu, CardsManagement):
            page_name = F.__name__
            frame = F(container=self.main_section, app=self)
            self.frames[page_name] = frame
            frame.grid(row=1, sticky="news", columnspan=2)

        navbar = Navbar(self)
        navbar.grid(row=0)

        self.main_section.grid(row=1, sticky="news", columnspan=2)
        self.main_section.grid_columnconfigure(0, weight=1)

        self.to("Menu")

    def to(self, frame_id):
        frame = self.frames[frame_id]
        frame.tkraise()
