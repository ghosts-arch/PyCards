from tkinter import Toplevel, Text, messagebox
from tkinter.ttk import Label, Button, Frame


class EditCardWindow(Toplevel):
    def __init__(self, master, card):
        super().__init__(background="#2d2d2d")

        self.master = master
        self.card = card

        self.resizable(False, False)
        self.grab_set()

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
        radio.insert("1.0", self.card.get("item")["values"][0])

        answer = Label(self, text="Reponse")
        answer.grid(row=3, padx=8, pady=8, sticky="w")

        radio = Text(
            self,
            name="answer_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        radio.grid(row=4, padx=8, pady=8)
        radio.insert("1.0", self.card.get("item")["values"][1])

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
            command=self.update_card,
            style="Success.TButton",
        )
        add_card_btn.grid(row=0, column=1, padx=8, pady=8)

    def update_card(self):
        question_entry = self.children.get("question_text")
        answer_entry = self.children.get("answer_text")
        question = question_entry.get("1.0", "end").strip()  # type: ignore
        answer = answer_entry.get("1.0", "end").strip()  # type: ignore
        if not question:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        if not answer:
            return messagebox.showerror("Erreur", 'Le champ "Réponse" est vide.')
        iid = self.card.get("id")
        self.master.update_card(iid, {"question": question, "answer": answer})  # type: ignore
        question_entry.delete("1.0", "end")
        answer_entry.delete("1.0", "end")

    def delete_card(self):
        iid = self.card.get("id")
        self.master.delete_card(iid)
        self.destroy()
