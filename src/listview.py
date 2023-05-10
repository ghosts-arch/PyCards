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
        self.insert("", "end", values=[*item])

    def update_item(self, item):
        focused = self.focus()
        print(focused)

    def delete_item(self, item):
        self.delete(item)

    def _item_selected(self, event):
        for selected_item in self.selection():
            EditCardWindow(self, question=selected_item)
