import re

from tkinter.ttk import (
    Frame,
    Label,
    Notebook,
    Treeview,
    Button,
)

from .edit_deck_window import EditDeckWindow


from .edit_card_frame import EditCardWindow

from .add_card_window import AddCardWindow


class CardsManagement(Frame):
    def __init__(self, container, app):
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
            self, columns=columns, show="tree headings", selectmode="browse"
        )

        for column in columns:
            self.tree.heading(column=column, text=column.capitalize(), anchor="w")

        self.tree.bind("<<TreeviewSelect>>", self._item_selected)

        self.tree.grid(row=1, sticky="news", padx=8, pady=8)

        for deck in container.master.decks:
            self.tree.insert(
                "", "end", text=deck["name"], iid=f"d-{deck['id']}", open=False
            )

        for cards in container.master.cards:
            self.insert_item(cards)

    def insert_item(self, card):
        self.tree.insert(
            "",
            "end",
            values=[card["question"], card["answer"]],
            iid=card["id"],
        )
        self.tree.move(card["id"], f"d-{card['deck_id']}", 0)

    def update_card(self, iid, question, answer):
        card = self.container.master.database.update_card(iid, question, answer)
        self.tree.item(iid, values=[card["question"], card["answer"]])

    def update_deck(self, iid, deck):
        deck = self.container.master.database.update_deck(iid, deck)
        self.tree.item(f'd-{deck["id"]}', text=deck["name"])

    def get_item_by_id(self, iid: str):
        items = [children for children in self.tree.get_children() if children == iid]
        return items

    def show_create_card_window(self):
        AddCardWindow(self)

    def update_cards_list(self, cards):
        self.container.master.cards.append(cards)
        for card in cards:
            self.insert_item(card)
            self.tree.move(card["id"], f"d-{card['deck_id']}", 0)

    def delete_card(self, iid):
        self.container.master.database.delete_card(iid)
        self.container.master.remove_card(iid)
        self.tree.delete(f"d-{iid}")

    def delete_deck(self, iid):
        self.container.master.database.delete_deck(iid)
        self.container.master.remove_deck(iid)
        print(iid)
        self.tree.delete(f"d-{iid}")

    def add_card(self, deck_id, question, answer):
        card = self.container.master.database.add_card(
            deck_id=deck_id, question=question, answer=answer
        )
        self.tree.insert(
            "",
            "end",
            values=[card["question"], card["answer"]],
            iid=card["id"],
        )
        self.tree.move(card["id"], f"d-{card['deck_id']}", 0)
        self.container.master.cards.append(card)

    def _item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            if re.match(r"d-\d{1,4}", selected_item):
                iid = re.findall(r"\d{1,4}", selected_item)[0]
                deck = self.container.master.get_deck_by_id(iid)
                return EditDeckWindow(master=self, deck=deck)
            EditCardWindow(self, iid=selected_item, item=item)
