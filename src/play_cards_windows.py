from tkinter import Toplevel, Text, messagebox
from tkinter.ttk import Label, Button
from random import choice


class PlayCardsWindow(Toplevel):
    def __init__(self, container):
        super().__init__(background="#2d2d2d")
        self.container = container
        self.resizable(False, False)
        self.grab_set()

        self.current_card = choice(self.container.master.master.cards)
        question_txt = Label(
            self,
            text=self.current_card["question"],
            font=("Lato", 12),
            name="question_txt",
        )
        question_txt.grid(row=0, sticky="w", padx=8, pady=8)
        response_input = Text(
            self,
            name="response_input",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
        )
        response_input.grid(row=3, padx=8, pady=8)
        validate_answer_btn = Button(
            self,
            text="Valider",
            command=self.validate_answer,
            name="validate_answer_btn",
        )
        validate_answer_btn.grid(padx=8, pady=8)
        Button(
            self,
            text="Nouvelle question",
            command=self.generate_question,
            name="generate_card_btn",
        )
        Label(self, name="hint_lbl")

    def validate_answer(self):
        hint_lbl = self.children.get("hint_lbl")
        validate_button = self.children.get("validate_answer_btn")
        new_question_btn = self.children.get("generate_card_btn")
        response_input = self.children.get("response_input")
        answer = response_input.get("1.0", "end").strip()
        if not answer:
            return messagebox.showerror("Erreur", 'Le champ "Réponse" est vide.')
        validate_button["state"] = "disabled"
        hint_lbl.grid(padx=8, pady=8)
        new_question_btn.grid(padx=8, pady=8)
        if answer == self.current_card["answer"]:
            hint_lbl["foreground"] = "green"
            hint_lbl["text"] = "Bonne reponse !"
        else:
            hint_lbl["foreground"] = "red"
            hint_lbl[
                "text"
            ] = f'Mauvaise reponse, la reponse correcte était "{self.current_card["answer"]}"'

    def generate_question(self):
        validate_button = self.children.get("validate_answer_btn")
        question_txt = self.children.get("question_txt")
        hint_lbl = self.children.get("hint_lbl")
        new_question_btn = self.children.get("generate_card_btn")

        hint_lbl.grid_forget()
        new_question_btn.grid_forget()
        self.current_card = choice(self.master.cards)
        question_txt["text"] = self.current_card["question"]
        validate_button["state"] = "normal"
