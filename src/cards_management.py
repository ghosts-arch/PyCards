from tkinter.ttk import (
    Frame,
    Label,
    Treeview,
    Button,
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
            self, text=f"Nombre de cartes - {len(self.container.master.cards)}"
        )
        card_count.grid(row=2, sticky="e", padx=8, pady=8)

        for cards in container.master.cards:
            self.insert_item(cards)

    def insert_item(self, card):
        self.tree.insert(
            "",
            "end",
            values=[card["question"], card["answer"]],
            iid=card["id"],
        )

    def update_card(self, iid, card):
        card = self.container.master.database.update_card(iid, card)
        self.tree.item(iid, values=[card["question"], card["answer"]])

    def get_item_by_id(self, iid: str):
        items = [children for children in self.tree.get_children() if children == iid]
        return items

    def show_create_card_window(self):
        AddCardWindow(self)

    def update_cards_list(self, cards):
        lbl = self.children.get("!label")
        self.container.master.cards.append(cards)
        lbl["text"] = f"Nombre de cartes - {len(self.container.master.cards)}"
        for card in cards:
            self.insert_item(card)

    def delete_card(self, iid):
        lbl = self.children.get("!label")
        self.container.master.database.delete_card(iid)
        self.container.master.remove_card(iid)
        self.tree.delete(iid)
        lbl["text"] = f"Nombre de cartes - {len(self.container.master.cards)}"

    def add_card(self, card):
        lbl = self.children.get("!label")
        card = self.container.master.database.add_card(
            {"question": card.get("question"), "answer": card.get("answer")}
        )
        # print(card)
        self.tree.insert(
            "",
            "end",
            values=[card["question"], card["answer"]],
            iid=card["id"],
        )
        self.container.master.cards.append(card)
        lbl["text"] = f"Nombre de cartes - {len(self.container.master.cards)}"

    def _item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            EditCardWindow(self, {"id": selected_item, "item": item})
