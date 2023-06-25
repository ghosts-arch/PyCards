from .menu import Home

from .root import Root


class View:
    def __init__(self):
        self._root = Root()
        self.frames = {}

        for F in (Home,):
            page_name = F.__name__
            self.frames[page_name] = F(parent=self._root)

    def to(self, frame_id):
        f = self.frames[frame_id]
        f.tkraise()
        f.grid(row=0, sticky="news")

    def start_main_loop(self):
        self._root.mainloop()
