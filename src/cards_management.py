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

        columns = ["question", "answer"]

        self.tree = Treeview(
            self, columns=columns, show="headings", selectmode="browse"
        )

        for column in columns:
            self.tree.heading(column=column, text=column.capitalize(), anchor="w")

        self.tree.bind("<<TreeviewSelect>>", self._item_selected)

        self.tree.grid(row=1, sticky="news", padx=8, pady=8)

        card_count = Label(
            self, text=f"Nombre de cartes - {len(self.container.master.questions)}"
        )
        card_count.grid(row=2, sticky="e", padx=8, pady=8)

        for question in container.master.questions:
            self.insert_item(question)

    def insert_item(self, item):
        values = [item.get("question"), item.get("answer")]
        item = self.tree.insert("", "end", values=values, iid=item["id"])

    def update_item(self, item):
        focused = self.focus()

    def get_item_by_id(self, iid: str):
        items = [children for children in self.tree.get_children() if children == iid]
        return items

    def show_create_card_window(self):
        AddCardWindow(self)

    def update_cards_list(self, cards):
        lbl = self.children.get("!label")
        self.container.master.questions.append(cards)
        lbl["text"] = f"Nombre de cartes - {len(self.container.master.questions)}"
        for card in cards:
            self.insert_item(card)

    def delete_card(self, iid):
        self.master.master.database.delete_card(iid)
        self.tree.delete(iid)

    def add_card(self, card):
        card = self.container.master.database.add_card(
            {"question": card.get("question"), "answer": card.get("answer")}
        )
        self.update_cards_list(card)

    def _item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            EditCardWindow(self, {"id": selected_item, "item": item})
