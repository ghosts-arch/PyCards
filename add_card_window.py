import tkinter as tk


class AddCardWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.master = master
        title = tk.Label(self,
                         text="Ajouter une carte",
                         font=("Arial", 24))
        title.pack()
        question_lbl = tk.Label(self, text="Question")
        question_lbl.pack()
        question_entry = tk.Entry(self)
        question_entry.pack()
        answer_lbl = tk.Label(self, text="Reponse")
        answer_lbl.pack()
        answer_entry = tk.Entry(self)
        answer_entry.pack()
        add_card_btn = tk.Button(
            self, text="Ajouter", command=self.add_card)
        add_card_btn.pack()

    def add_card(self):
        print(self.children)
        question_entry = self.children.get("!entry")
        answer_entry = self.children.get("!entry2")
        question = question_entry.get()
        answer = answer_entry.get()
        self.master.questions.append({  # type: ignore
            "question": question,
            "answer": answer
        })
        self.master.update_cards_list()  # type: ignore
