from tkinter import EXTENDED, Listbox, StringVar, Text, Variable
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox, Frame, Label, OptionMenu, Treeview, Scrollbar, Button

from .listview import ListView

from .edit_card_frame import EditCardWindow

from .add_card_window import AddCardWindow


class CardsManagement(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)

        left_frame = Frame(self, name="left_frame")
        left_frame.grid(column=0, row=0, padx=8, pady=8)

        right_frame = Frame(self, name="right_frame")
        right_frame.grid(column=1, row=0, padx=8, pady=8)

        deck_select_label = Label(left_frame, text="Deck")
        deck_select_label.grid(row=0, padx=8, pady=8)
        # create a list box
        langs = ("deck 1", "deck 2", "deck 3")

        var = StringVar(self)

        listbox = Combobox(left_frame, state="readonly")
        listbox["values"] = langs
        listbox.grid(row=1, sticky="ew", padx=8, pady=8)

        collection_size_string = f"Nombre de cartes - {len(container.master.questions)}"
        cards_collection_size_lbl = Label(left_frame, text=collection_size_string)
        cards_collection_size_lbl.grid(row=2, padx=8, pady=8)

        self.tree = ListView(
            left_frame, columns=("id", "question", "answer"), show="headings"
        )

        self.tree.grid(row=3, padx=(8, 0), pady=8)

        scrollbar = Scrollbar(left_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=3, column=1, sticky="ns", padx=(0, 8), pady=8)

        for question in container.master.questions:
            self.tree.insert_item(question)

        question = Label(right_frame, text="Question")
        question.grid(row=0, sticky="w", padx=8, pady=8)

        question_text = Text(right_frame, height=8, name="question_text")
        question_text.grid(row=1, padx=8, pady=8)

        answer = Label(right_frame, text="Reponse")
        answer.grid(row=2, padx=8, pady=8, sticky="w")

        answer_text = Text(right_frame, height=8, name="answer_text")
        answer_text.grid(row=3, padx=8, pady=8)

        buttons_group = Frame(right_frame)
        buttons_group.grid(row=4, sticky="e")
        add_card_btn = Button(buttons_group, text="Annuler", command=self.add_card)
        add_card_btn.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        add_card_btn = Button(buttons_group, text="Ajouter", command=self.add_card)
        add_card_btn.grid(row=0, column=1, padx=8, pady=8)

    def delete_card(
        self,
    ):
        self.tree.delete_item(self.tree.selection())

    def show_create_card_window(self):
        AddCardWindow(self)

    def update_cards_list(self, cards):
        left_frame = self.children.get("left_frame")
        lbl = left_frame.children.get("!label")
        self.container.master.questions.append(cards)
        lbl["text"] = f"Nombre de cartes - {len(self.container.master.questions)}"
        for card in cards:
            self.tree.insert_item(card.values())

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
