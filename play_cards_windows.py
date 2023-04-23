import tkinter as tk
from tkinter.ttk import Separator
from random import choice


class PlayCardsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.current_card = choice(self.master.questions)
        question_txt = tk.Label(self,
                                text=self.current_card["question"], font=("Arial", 12), name="question_txt")
        question_txt.pack()
        separator = Separator(self, orient="horizontal")
        separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)
        response_input = tk.Entry(self, name="response_input")
        response_input.pack()
        validate_answer_btn = tk.Button(self,
                                        text="Valider", command=self.validate_answer)
        validate_answer_btn.pack()
        tk.Button(self, text="Nouvelle question",
                  command=self.generate_question)
        tk.Label(self, name="hint_lbl")

    def validate_answer(self):
        hint_lbl = self.children.get("hint_lbl")
        new_question_btn = self.children.get("!button2")
        response_input = self.children.get("response_input")
        hint_lbl.pack()
        answer = response_input.get()
        new_question_btn.pack()
        if answer == self.current_card["answer"]:
            hint_lbl["foreground"] = "green"
            hint_lbl["text"] = "Bonne reponse !"
        else:
            hint_lbl["foreground"] = "red"
            hint_lbl["text"] = f"Mauvaise reponse, la reponse correcte était {self.current_card['answer']}"

    def generate_question(self):
        question_txt = self.children.get("question_txt")
        hint_lbl = self.children.get("hint_lbl")
        new_question_btn = self.children.get("!button2")

        hint_lbl.pack_forget()
        new_question_btn.pack_forget()
        self.current_card = choice(self.master.questions)
        question_txt["text"] = self.current_card["question"]
