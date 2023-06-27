from tkinter import ttk


class Editor(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self._current_card = None
        self._controller = None

        self.columnconfigure(0, weight=1)

        self.header_frame = ttk.Frame(self)
        self.header_frame.rowconfigure(0, weight=1)
        self.header_frame.rowconfigure(1, weight=1)
        self.header_frame.columnconfigure(1, weight=1)

        self.header_frame.grid(row=0, sticky="news", padx=8, pady=8)

        self.to_menu_button = ttk.Button(self.header_frame, text="Menu")
        self.to_menu_button.grid(row=0, column=0, padx=8, pady=8, sticky="w")

        self.delete_deck_button = ttk.Button(
            self.header_frame,
            text="Supprimer",
            style="Danger.TButton",
        )
        self.delete_deck_button.grid(row=0, column=2, sticky="e", padx=8, pady=8)

        self.new_card_button = ttk.Button(
            self, text="Nouvelle carte", style="Success.TButton"
        )
        self.new_card_button.grid(column=0, row=1, padx=16, pady=8, sticky="e")

        container = ttk.Frame(self)
        container.grid(row=2, sticky="news", padx=8, pady=8)
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        left_column = ttk.Frame(container)
        left_column.grid(row=0, column=0, sticky="news", padx=8, pady=8)

        columns = ["question", "answer"]
        self.tree = ttk.Treeview(left_column, columns=columns, show="headings")

        for column in columns:
            self.tree.heading(column=column, text=column.capitalize(), anchor="center")

        self.tree.grid(row=0, column=0, sticky="news", padx=8, pady=8)

        scrollbar = ttk.Scrollbar(
            left_column, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.right_column = ttk.Frame(container)
        self.right_column.grid(
            row=0, column=1, columnspan=3, padx=8, pady=8, sticky="en"
        )
