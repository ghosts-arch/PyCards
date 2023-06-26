from random import choice
from tkinter import ttk
import tkinter


class Player(ttk.Frame):
    def __init__(self, parent, deck):
        super().__init__(parent)
        self.deck = deck

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.header_frame = ttk.Frame(self)
        self.header_frame.rowconfigure(0, weight=1)
        self.header_frame.rowconfigure(1, weight=1)
        self.header_frame.columnconfigure(1, weight=1)

        self.header_frame.grid(row=0, sticky="news", padx=8, pady=8)

        self.to_menu_button = ttk.Button(self.header_frame, text="Menu")
        self.to_menu_button.grid(row=0, column=0, padx=8, pady=8, sticky="w")

        self.card_container = ttk.Frame(self, relief="groove")
        self.card_container.grid(row=1, padx=8, pady=8, sticky="news")
        self.card_container.columnconfigure(0, weight=1)
        self.card_container.rowconfigure(0, weight=1)

        self.question_txt = ttk.Label(
            self.card_container,
            font=("Lato", 12),
            name="question_txt",
        )
        self.question_txt.grid(row=0, padx=8, pady=8)

        self.response_input = tkinter.Text(
            self,
            name="response_input",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
        )
        self.response_input.grid(row=2, padx=8, pady=8, sticky="news")

        self.hint_label = ttk.Label(self, name="hint_lbl")

        buttons_group = ttk.Frame(self)
        buttons_group.grid(row=3)

        self.skip_card_button = ttk.Button(
            buttons_group,
            text="Passer",
            style="Warning.TButton",
        )
        self.skip_card_button.grid(row=0, column=0, padx=8, pady=8)

        self.validate_answer_button = ttk.Button(
            buttons_group,
            text="Valider",
            style="Success.TButton",
        )
        self.validate_answer_button.grid(row=0, column=1, padx=8, pady=8)

        self.new_card_button = ttk.Button(
            buttons_group,
            text="Nouvelle question",
            name="generate_card_btn",
        )
