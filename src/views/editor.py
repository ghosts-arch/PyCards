from tkinter import ttk


class Editor(ttk.Frame):
    def __init__(self, container, app):
        super().__init__(container)

        self.treeview = ttk.Treeview(self)
        self.grid(row=0)
