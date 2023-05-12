from tkinter.ttk import Treeview
from typing import Literal

from .edit_card_frame import EditCardWindow


class ListView(Treeview):
    def __init__(self, master, columns, show):
        super().__init__(master=master, show=show, columns=columns, selectmode="browse")
        for column in columns:
            self.heading(column=column, text=column.capitalize(), anchor="w")
        self.bind("<<TreeviewSelect>>", self._item_selected)

    def insert_item(self, item):
        id = item.get("id")
        values = [item.get("question"), item.get("answer")]
        self.insert("", "end", values=values, iid=str(id))

    def update_item(self, item):
        focused = self.focus()

    def delete_item(self, item):
        self.delete(item)

    def _item_selected(self, event):
        for selected_item in self.selection():
            item = self.item(selected_item)
            EditCardWindow(self, question=item)
