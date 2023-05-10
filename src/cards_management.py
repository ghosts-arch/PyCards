from tkinter import EXTENDED, Listbox, StringVar, Text, Variable
from tkinter.messagebox import showinfo
from tkinter.ttk import (
    Combobox,
    Frame,
    Label,
    OptionMenu,
    Treeview,
    Scrollbar,
    Button,
    Entry,
)

from .listview import ListView

from .edit_card_frame import EditCardWindow

from .add_card_window import AddCardWindow


class CardsManagement(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        button = Button(
            self,
            text="Ajouter",
            style="Success.TButton",
            command=self.show_create_card_window,
        )
        button.grid(row=0, sticky="e", padx=8, pady=8)
        self.tree = ListView(self, columns=("question", "answer"), show="headings")

        self.tree.grid(row=1, sticky="news", padx=8, pady=8)

        card_count = Label(
            self, text=f"Nombre de cartes - {len(self.container.master.questions)}"
        )
        card_count.grid(row=2, sticky="e", padx=8, pady=8)

        for question in container.master.questions:
            self.tree.insert_item((question.get("question"), question.get("answer")))

    def delete_card(
        self,
    ):
        self.tree.delete_item(self.tree.selection())

    def show_create_card_window(self):
        AddCardWindow(self)

    def update_cards_list(self, cards):
        lbl = self.children.get("!label")
        self.container.master.questions.append(cards)
        lbl["text"] = f"Nombre de cartes - {len(self.container.master.questions)}"
        for card in cards:
            self.tree.insert_item((card.get("question"), card.get("answer")))

    def add_card(self):
        right_frame = self.children.get("right_frame")
        question_entry = right_frame.children.get("question_text")
        answer_entry = right_frame.children.get("answer_text")
        question = question_entry.get("1.0", "end")  # type: ignore
        answer = answer_entry.get("1.0", "end")  # type: ignore
        print(self.container)
        card = self.container.master.database.add_card(
            {"question": question, "answer": answer}
        )
        self.update_cards_list(card)  # type: ignore
        question_entry.delete("1.0", "end")
        answer_entry.delete("1.0", "end")
