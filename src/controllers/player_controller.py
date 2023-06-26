from random import choice
from tkinter import messagebox
from ..views.view import View
from ..models.model import Model


class PlayerController:
    def __init__(self, model: Model, view: View, deck) -> None:
        self.model = model
        self.view = view
        self.deck = deck
        self.frame = self.view.frames["Player"]
        self.current_card = self.generate_random_card()
        self.bind()
        self.display_card(self.current_card)

    def bind(self):
        self.frame.to_menu_button.config(command=self.back_to_home)
        self.frame.skip_card_button.config(command=self.skip_card)
        self.frame.validate_answer_button.config(command=self.validate_answer)
        self.frame.new_card_button.config(command=self.generate_question)

    def back_to_home(self):
        self.view.to("Home")

    def generate_random_card(self):
        return choice(self.deck.cards)

    def display_card(self, card):
        self.frame.question_txt.config(text=card.question)

    def skip_card(self):
        self.current_card = self.generate_random_card()
        self.display_card(self.current_card)

    def validate_answer(self):
        hint_lbl = self.frame.hint_label
        # validate_button = self.children.get("validate_answer_btn")
        # new_question_btn = self.children.get("generate_card_btn")
        # response_input = self.children.get("response_input")
        answer = self.frame.response_input.get("1.0", "end").strip()
        if not answer:
            return messagebox.showerror("Erreur", 'Le champ "Réponse" est vide.')
        self.frame.validate_answer_button.config(state="disabled")
        self.frame.skip_card_button.config(state="disabled")

        hint_lbl.grid(padx=8, pady=8)
        self.frame.new_card_button.grid(row=0, column=1, padx=8, pady=8)
        # self.frame.new_question_btn.grid(padx=8, pady=8)
        if answer == self.current_card.answer:
            hint_lbl["foreground"] = "green"
            hint_lbl["text"] = "Bonne reponse !"
        else:
            hint_lbl["foreground"] = "red"
            hint_lbl[
                "text"
            ] = f'Mauvaise reponse, la reponse correcte était "{self.current_card.answer}"'

    def generate_question(self):
        # validate_button = self.children.get("validate_answer_btn")
        # question_txt = self.children.get("question_txt")
        # hint_lbl = self.children.get("hint_lbl")
        # new_question_btn = self.children.get("generate_card_btn")

        self.frame.hint_label.grid_forget()
        self.frame.new_card_button.grid_forget()
        self.current_card = choice(self.deck.cards)
        self.frame.question_txt["text"] = self.current_card.question
        self.frame.validate_answer_button["state"] = "normal"
        self.frame.skip_card_button["state"] = "normal"
        self.frame.response_input.delete("1.0", "end")
