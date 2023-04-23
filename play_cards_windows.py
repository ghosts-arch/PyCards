import tkinter as tk


class PlayCardsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.master = master
        question_txt = tk.Label(
            text=randomQuestion["question"], font=("Arial", 12))
        question_txt.pack()
        response_input = tk.Entry()
        response_input.pack()
        validate_answer_btn = tk.Button(
            text="Valider", command=validate_answer)
        validate_answer_btn.pack()
        new_question_btn = tk.Button(text="Nouvelle question",
                                     command=generate_question)
        hint_lbl = tk.Label()


def add_card(self):
    print(self.children)
    question_entry = self.children.get("!entry")
    answer_entry = self.children.get("!entry2")
    question = question_entry.get()  # type: ignore
    answer = answer_entry.get()  # type: ignore
    self.master.questions.append({  # type: ignore
        "question": question,
        "answer": answer
    })
    self.master.update_cards_list()  # type: ignore
