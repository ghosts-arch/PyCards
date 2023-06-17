from tkinter import ttk
from .editor import Editor
from .menu import Home

from .root import Root


class View:
    def __init__(self):
        self._root = Root()
        self.frames = {}

        for F in (Home, Editor):
            page_name = F.__name__
            self.frames[page_name] = F(self._root)

    def to(self, frame_id):
        f = self.frames[frame_id]
        f.tkraise()
        f.grid(row=0, sticky="news")

    def to_editor(self, deck):
        f = Editor(self, app=self, deck=deck)

        f.tkraise()

        f.grid(row=0, sticky="news")

    def start_main_loop(self):
        self._root.mainloop()
