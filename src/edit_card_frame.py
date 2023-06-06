from tkinter import Toplevel, Text, messagebox
from tkinter.ttk import Label, Button, Frame


class EditCardWindow(Toplevel):
    def __init__(self, container, iid: str, item):
        super().__init__(background="#2d2d2d")

        self.container = container
        self.iid = iid
        self.item = item

        self.resizable(False, False)
        self.grab_set()

        title = Label(self, text="Editer une carte")
        title.grid(row=0, column=0, padx=8, pady=8)

        self.question_label = Label(self, text="Question")
        self.question_label.grid(row=1, padx=8, pady=8, sticky="w")

        self.question_text = Text(
            self,
            name="question_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        self.question_text.grid(row=2, padx=8, pady=8)
        self.question_text.insert("1.0", self.item["values"][0])

        answer_label = Label(self, text="Reponse")
        answer_label.grid(row=3, padx=8, pady=8, sticky="w")

        self.answer_text = Text(
            self,
            name="answer_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        self.answer_text.grid(row=4, padx=8, pady=8)
        self.answer_text.insert("1.0", self.item["values"][1])

        buttons_group = Frame(self)
        buttons_group.grid(row=5, sticky="e")

        delete_card_button = Button(
            buttons_group,
            text="Supprimer",
            command=self.delete_card,
            style="Danger.TButton",
        )
        delete_card_button.grid(row=0, column=0, padx=8, pady=8, sticky="e")

        update_card_button = Button(
            buttons_group,
            text="Valider",
            command=self.update_card,
            style="Success.TButton",
        )
        update_card_button.grid(row=0, column=1, padx=8, pady=8)

    def update_card(self):
        question = self.question_text.get("1.0", "end").strip()
        answer = self.answer_text.get("1.0", "end").strip()
        if not question:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        if not answer:
            return messagebox.showerror("Erreur", 'Le champ "Réponse" est vide.')
        self.container.update_card(self.iid, question=question, answer=answer)
        self.question_text.delete("1.0", "end")
        self.answer_text.delete("1.0", "end")

    def delete_card(self):
        self.container.delete_card(self.iid)
        self.destroy()
