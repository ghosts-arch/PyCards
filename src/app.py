from tkinter import Tk, messagebox
from tkinter.ttk import Button, Style, Notebook, Frame
from src.play_cards_windows import PlayCardsWindow
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
            "background": [
                ("active", "darkblue"),
            ],
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
    "Default.TButton": {
        "configure": {"background": "grey"},
        "map": {
            "background": [
                ("active", "darkgrey"),
            ],
        },
    },
    "TNotebook.Tab": {"map": {"background": [("selected", "blue")]}},
    "Treeview": {
        "configure": {
            "font": ("Lato", 12),
            "background": "#4d4d4d",
            "borderwidth": 0,
            "fieldbackground": "#4d4d4d",
        },
        "map": {"background": [("selected", "#6d6d6d")]},
    },
    "Treeview.treearea": {"configure": {"foreground": "red"}},
}


class App(Tk):
    def __init__(self):
        super().__init__()
        self.database = Database()
        self.questions = self.database.get_cards()
        self.title("PyCards")
        self.state("zoomed")
        self.configure(background="blue")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

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

        notebook = Notebook(self)
        notebook.grid(row=0, column=0, sticky="news")

        main_menu = MainMenu(notebook)
        cards_management = CardsManagement(notebook)

        main_menu.grid()
        cards_management.grid()

        notebook.add(main_menu, text="Menu Principal")
        notebook.add(cards_management, text="Gerer les cartes")
