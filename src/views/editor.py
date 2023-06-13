from tkinter import Text, messagebox, ttk

from .view import View


class Editor(View):
    def __init__(self, container, app, deck):
        super().__init__(container, app)
        self._app = app
        self._container = container
        self._deck = deck
        self._current_card = None

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid(row=1, sticky="news", columnspan=2)

        header_frame = ttk.Frame(self)
        header_frame.rowconfigure(0, weight=1)
        header_frame.columnconfigure(1, weight=1)

        header_frame.grid(row=0, padx=8, pady=8)

        header_frame.grid(row=0, sticky="news", padx=8, pady=8, columnspan=2)

        card_title = ttk.Label(
            header_frame, text=self._deck.name, font=("Lato", 24, "bold")
        )
        card_title.grid(row=0, column=0, padx=8, pady=8)

        delete_button = ttk.Button(
            header_frame, text="Supprimer", style="Danger.TButton"
        )
        delete_button.grid(row=0, column=1, sticky="e", padx=8, pady=8)

        container = ttk.Frame(self)
        container.grid(row=1, columnspan=2, sticky="news", padx=8, pady=8)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=3)

        left_column = ttk.Frame(container)
        left_column.grid(row=0, column=0, sticky="news", padx=8, pady=8)

        columns = ["question", "answer"]
        self.tree = ttk.Treeview(left_column, columns=columns, show="headings")

        for column in columns:
            self.tree.heading(column=column, text=column.capitalize(), anchor="center")

        for card in self._deck.cards:
            self.tree.insert(
                "",
                "end",
                values=[card.question, card.answer],
                iid=card.iid,
            )

        self.tree.bind("<<TreeviewSelect>>", self._item_selected)
        self.tree.grid(row=0, column=0, sticky="news")

        self.editor_button = ttk.Button(
            left_column,
            text="Gerer les cartes",
        )
        self.editor_button.grid(row=1, column=0, padx=(4, 4), pady=8)

        right_column = ttk.Frame(container)
        right_column.grid(row=0, column=1, sticky="news")

        edit_card_form = ttk.Frame(right_column)
        edit_card_form.grid(column=0, row=0)

        card_question_label = ttk.Label(edit_card_form, text="Question")
        card_question_label.grid(row=0, column=0, sticky="w", padx=8, pady=8)

        self.question_text = Text(
            edit_card_form,
            name="question_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
            state="disabled",
        )
        self.question_text.grid(
            column=0,
            row=1,
            padx=8,
            pady=8,
        )

        card_answer_label = ttk.Label(edit_card_form, text="Reponse")
        card_answer_label.grid(row=9, column=0, sticky="w", padx=8, pady=8)

        self.answer_text = Text(
            edit_card_form,
            name="question_answer",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
            state="disabled",
        )
        self.answer_text.grid(column=0, row=19, padx=8, pady=8)

        buttons_group = ttk.Frame(right_column)
        buttons_group.grid(row=2, sticky="e")

        delete_card_button = ttk.Button(
            buttons_group,
            text="Supprimer",
            style="Danger.TButton",
        )
        delete_card_button.grid(row=0, column=0, padx=8, pady=8, sticky="w")

        update_card_button = ttk.Button(
            buttons_group,
            text="Valider",
            style="Success.TButton",
            command=lambda: self.update_card(self._current_card),
        )
        update_card_button.grid(row=0, column=1, padx=8, pady=8, sticky="e")

    def _item_selected(self, event):
        for selected_item in self.tree.selection():
            card = self._deck.get_card_by_iid(selected_item)
            self._current_card = card
            self.edit_card(card)

    def edit_card(self, card):
        self.question_text.configure(state="normal")
        self.question_text.insert("1.0", card.question)
        self.answer_text.configure(state="normal")
        self.answer_text.insert("1.0", card.answer)

    def update_card(self, card):
        question = self.question_text.get("1.0", "end").strip()
        answer = self.answer_text.get("1.0", "end").strip()
        if not question:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        if not answer:
            return messagebox.showerror("Erreur", 'Le champ "Réponse" est vide.')
        card = self._app.database.update_card(card.iid, question, answer)
        self.tree.item(card.iid, values=[card.question, card.answer])
        self.question_text.delete("1.0", "end")
        self.answer_text.delete("1.0", "end")
