from tkinter import Tk
from tkinter.ttk import Style
from ..themes.dark_theme import dark_theme


class Root(Tk):
    def __init__(self):
        super().__init__()

        self.title("PyCards")
        self.state("zoomed")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        s = Style()
        s.theme_create("dark", parent="default", settings=dark_theme)
        s.theme_use("dark")
