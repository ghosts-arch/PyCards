from tkinter.ttk import Button, Frame


class Navbar(Frame):
    def __init__(self, container) -> None:
        super().__init__()
        self.container = container

        self.buttons_group = Frame(self.container)
        self.buttons_group.rowconfigure(0, weight=1)
        self.buttons_group.columnconfigure(0, weight=1)
        self.buttons_group.columnconfigure(1, weight=1)
        self.buttons_group.grid(sticky="news")

        self.main_menu_button = Button(
            self.buttons_group,
            text="Menu Principal",
        )
        self.main_menu_button.grid(row=0, column=0, padx=(8, 4), pady=8, sticky="e")

        self.editor_button = Button(
            self.buttons_group,
            text="Gerer les cartes",
            command=self.container.to("editor"),
        )
        self.editor_button.grid(row=0, column=1, padx=(4, 8), pady=8, sticky="w")
