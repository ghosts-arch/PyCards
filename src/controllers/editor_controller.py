from tkinter import ttk


from ..models.model import Model
from ..views.view import View


class EditorController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["Editor"]
        self.bind()

    def bind(self):
        self.frame.to_menu_button.config(command=self.back_to_home)
        self.frame.deck_name_entry.bind("<FocusOut>", self.save_deck)

    def back_to_home(self):
        self.view.to("Home")

    def save_deck(self, event):
        deck_name = self.frame.deck_name_entry.get()
        deck = self.model.decks.create_deck(deck_name=deck_name)
        self.frame.deck_name_entry.destroy()
        self.deck_title = ttk.Label(
            self.frame.header_frame,
            text=deck.name,
            font=("Lato", 24, "bold"),
        )
        self.deck_title.grid(row=0, column=1, padx=8, pady=8, sticky="w")
