from tkinter.ttk import Button, Frame


class Navbar(Frame):
    def __init__(self, container) -> None:
        super().__init__()
        self.container = container

        self.buttons_group = Frame(self.container)
        self.buttons_group.rowconfigure(0, weight=1)
        self.buttons_group.columnconfigure(0, weight=1)
        self.buttons_group.columnconfigure(2, weight=1)

        self.buttons_group.grid(sticky="news")

        self.main_menu_button = Button(
            self.buttons_group,
            text="Menu Principal",
            command=lambda: self.container.to("Menu"),
        )
        self.main_menu_button.grid(row=0, column=0, padx=(8, 4), pady=8, sticky="e")

        self.editor_button = Button(
            self.buttons_group,
            text="Gerer les cartes",
            command=lambda: self.container.to("CardsManagement"),
        )
        self.editor_button.grid(row=0, column=1, padx=(4, 4), pady=8, sticky="w")

        self.editor_button = Button(
            self.buttons_group,
            text="Gerer les cartes",
            command=lambda: self.container.to("Editor"),
        )
        self.editor_button.grid(row=0, column=2, padx=(4, 8), pady=8, sticky="w")
