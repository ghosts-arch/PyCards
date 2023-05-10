from tkinter import Toplevel, Text
from tkinter.ttk import Label, Entry, Button, LabelFrame, Frame, Style


class EditCardWindow(Toplevel):
    def __init__(self, master, question):
        super().__init__(background="#2d2d2d")

        self.master = master
        self.question = question

        self.resizable(False, False)
        self.grab_set()

        print(self.question)
        title = Label(self, text="Editer une carte")
        title.grid(row=0, column=0, padx=8, pady=8)

        question = Label(self, text="Question")
        question.grid(row=1, padx=8, pady=8, sticky="w")

        radio = Text(
            self,
            name="question_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        radio.grid(row=2, padx=8, pady=8)
        radio.insert("1.0", self.question["values"][0])

        answer = Label(self, text="Reponse")
        answer.grid(row=3, padx=8, pady=8, sticky="w")

        radio = Text(
            self,
            name="question_answer",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        radio.grid(row=4, padx=8, pady=8)
        radio.insert("1.0", self.question["values"][1])

        buttons_group = Frame(self)
        buttons_group.grid(row=5, sticky="e")
        add_card_btn = Button(
            buttons_group,
            text="Supprimer",
            command=self.delete_card,
            style="Danger.TButton",
        )
        add_card_btn.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        add_card_btn = Button(
            buttons_group,
            text="Valider",
            command=self.add_card,
            style="Success.TButton",
        )
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
        question_entry = self.children.get("!entry")
        answer_entry = self.children.get("!entry2")
        question = question_entry.get()  # type: ignore
        answer = answer_entry.get()  # type: ignore
        card = self.master.database.add_card({"question": question, "answer": answer})
        self.master.update_cards_list(card)  # type: ignore
        question_entry.delete(0, "end")
        answer_entry.delete(0, "end")

    def delete_card(self):
        pass
