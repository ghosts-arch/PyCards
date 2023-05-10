from tkinter import Toplevel, Text
from tkinter.ttk import Label, Entry, Button, LabelFrame, Frame


class AddCardWindow(Toplevel):
    def __init__(self, container):
        super().__init__()
        self.container = container
        self.resizable(False, False)
        self.grab_set()

        title = Label(self, text="Ajouter une carte")
        title.grid(row=0, column=0, padx=8, pady=8)

        question = Label(self, text="Question")
        question.grid(row=1, padx=8, pady=8, sticky="w")

        radio = Text(self, height=8)
        radio.grid(row=2, padx=8, pady=8)

        answer = Label(self, text="Reponse")
        answer.grid(row=3, padx=8, pady=8, sticky="w")

        radio = Text(self, height=8)
        radio.grid(row=4, padx=8, pady=8)

        buttons_group = Frame(self)
        buttons_group.grid(row=5, sticky="e")
        add_card_btn = Button(buttons_group, text="Annuler", command=self.add_card)
        add_card_btn.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        add_card_btn = Button(buttons_group, text="Ajouter", command=self.add_card)
        add_card_btn.grid(row=0, column=1, padx=8, pady=8)

        """
        question_lbl = Label(self, text="Question")
        question_lbl.grid()
        question_entry = Text(self, height=8)
        question_entry.grid()
        answer_lbl = Label(self, text="Reponse")
        answer_lbl.grid()
        answer_entry = Entry(self)
        answer_entry.grid()
        add_card_btn = Button(self, text="Ajouter", command=self.add_card)
        add_card_btn.grid()
        """

    def add_card(self):
        question_entry = self.children.get("!text")
        answer_entry = self.children.get("!text2")
        question = question_entry.get("1.0", "end")  # type: ignore
        answer = answer_entry.get("1.0", "end")  # type: ignore
        print(self.container)
        card = self.container.master.master.database.add_card(
            {"question": question, "answer": answer}
        )
        self.container.update_cards_list(card)  # type: ignore
        question_entry.delete(0, "end")
        answer_entry.delete(0, "end")
