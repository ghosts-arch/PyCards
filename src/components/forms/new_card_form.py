from tkinter import ttk, Text


class NewCardForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        card_question_label = ttk.Label(self, text="Question")
        card_question_label.grid(row=0, column=0, sticky="w", padx=8, pady=8)

        self.question_text = Text(
            self,
            name="question_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        self.question_text.grid(
            column=0,
            row=1,
            padx=8,
            pady=8,
        )

        card_answer_label = ttk.Label(self, text="Reponse")
        card_answer_label.grid(row=9, column=0, sticky="w", padx=8, pady=8)

        self.answer_text = Text(
            self,
            name="question_answer",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        self.answer_text.grid(column=0, row=19, padx=8, pady=8)

        buttons_group = ttk.Frame(self)
        buttons_group.grid(row=20, sticky="e")

        self.cancel_button = ttk.Button(
            buttons_group,
            text="Supprimer",
            style="Danger.TButton",
        )
        self.cancel_button.grid(row=0, column=0, padx=8, pady=8, sticky="w")

        self.create_card_button = ttk.Button(
            buttons_group,
            text="Valider",
            style="Success.TButton",
        )
        self.create_card_button.grid(row=0, column=1, padx=8, pady=8, sticky="e")
