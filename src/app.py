from tkinter import Tk, messagebox
from tkinter.ttk import Button, Style, Notebook, Frame
from src.play_cards_windows import PlayCardsWindow
from .database import Database
from .cards_management import CardsManagement
from .main_menu import MainMenu


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
        s.configure("TButton", font=("Lato", 12))
        s.configure("TLabel", font=("Lato", 12))
        s.configure("Treeview.Heading", font=("Lato", 12))
        s.configure("TNotebook.Tab", font=("Lato", 12), padding=[8, 8, 8, 8])
        s.configure(
            "TNotebook", tabposition="n", font=("Lato", 65), tabmargins=[8, 8, 8, 8]
        )

        notebook = Notebook(self)
        notebook.grid(row=0, column=0, sticky="news")

        main_menu = MainMenu(notebook)
        cards_management = CardsManagement(notebook)
        settings = Frame(notebook)

        main_menu.grid()
        cards_management.grid()
        settings.grid()

        notebook.add(main_menu, text="Menu Principal")
        notebook.add(cards_management, text="Gerer les cartes")
        notebook.add(settings, text="Parametres")
