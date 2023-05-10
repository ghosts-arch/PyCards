from tkinter import messagebox
from tkinter.ttk import Button, Frame

from .play_cards_windows import PlayCardsWindow


class MainMenu(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        start_btn = Button(self, text="Demarrer", command=self.show_play_cards_window)

        start_btn.grid(row=0, padx=8, pady=8)

    def show_play_cards_window(self):
        if not len(self.container.master.questions):
            return messagebox.showerror("Erreur", "Aucune carte trouvée !")
        PlayCardsWindow(self)
