from tkinter import Toplevel, Text
from tkinter.ttk import Label, Entry, Button, LabelFrame, Frame


class AddCardWindow(Toplevel):
    def __init__(self, container):
        super().__init__(background="#2d2d2d")
        self.container = container
        self.resizable(False, False)
        self.grab_set()

        question = Label(self, text="Question")
        question.grid(row=0, sticky="w", padx=8, pady=8)

        question_text = Text(
            self,
            name="question_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        question_text.grid(row=1, padx=8, pady=8)

        answer = Label(self, text="Reponse")
        answer.grid(row=2, padx=8, pady=8, sticky="w")

        answer_text = Text(
            self,
            name="answer_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        answer_text.grid(row=3, padx=8, pady=8)

        buttons_group = Frame(self)
        buttons_group.grid(row=4, sticky="e")
        add_card_btn = Button(
            buttons_group,
            text="Annuler",
            command=self.close_window,
            style="Default.TButton",
        )
        add_card_btn.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        add_card_btn = Button(
            buttons_group,
            text="Ajouter",
            command=self.add_card,
            style="Success.TButton",
        )
        add_card_btn.grid(row=0, column=1, padx=8, pady=8)

    def close_window(self):
        self.destroy()

    def add_card(self):
        question_entry = self.children.get("question_text")
        answer_entry = self.children.get("answer_text")
        question = question_entry.get("1.0", "end")  # type: ignore
        answer = answer_entry.get("1.0", "end")  # type: ignore
        print(self.container)
        card = self.container.master.master.database.add_card(
            {"question": question, "answer": answer}
        )
        self.container.update_cards_list(card)  # type: ignore
        question_entry.delete("1.0", "end")
        answer_entry.delete("1.0", "end")
