from tkinter import ttk


class View(ttk.Frame):
    def __init__(self, container, app, *args, **kargs):
        super().__init__(container)
