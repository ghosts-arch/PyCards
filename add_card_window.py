import tkinter as tk
from tkinter.ttk import Label, Entry, Button


class AddCardWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.master = master
        title = Label(self,
                      text="Ajouter une carte",
                      font=("Arial", 24))
        title.pack()
        question_lbl = Label(self, text="Question")
        question_lbl.pack()
        question_entry = Entry(self)
        question_entry.pack()
        answer_lbl = Label(self, text="Reponse")
        answer_lbl.pack()
        answer_entry = Entry(self)
        answer_entry.pack()
        add_card_btn = Button(
            self, text="Ajouter", command=self.add_card)
        add_card_btn.pack()

    def add_card(self):
        question_entry = self.children.get("!entry")
        answer_entry = self.children.get("!entry2")
        tree = self.master.children.get("!treeview")
        question = question_entry.get()  # type: ignore
        answer = answer_entry.get()  # type: ignore
        self.master.questions.append({  # type: ignore
            "question": question,
            "answer": answer
        })
        tree.insert('', tk.END, values=(question, answer))
        self.master.update_cards_list()  # type: ignore
        question_entry.delete(0, "end")
        answer_entry.delete(0, "end")
