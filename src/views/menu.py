from tkinter import ttk

from tkinter.ttk import Button
from ..components.decks_grid import DecksGrid


class Home(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)

        self.centered_frame = ttk.Frame(self)
        self.centered_frame.grid(row=0)

        self.app_title_label = ttk.Label(
            self.centered_frame, text="PyCards", font=("Lato", 24, "bold")
        )
        self.app_title_label.grid(row=0, padx=8, pady=8)

        self.decks_grid = DecksGrid(
            self.centered_frame,
            self,
            no_content_message="Vous n'avez aucun deck actuellement.",
        )

        self.decks_grid.grid(row=1)

        self.add_deck_button = Button(
            self.centered_frame, text="Ajouter un deck", style="Success.TButton"
        )
        self.add_deck_button.grid(row=2, padx=8, pady=8)
