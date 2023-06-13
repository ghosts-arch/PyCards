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

        self.header_frame = ttk.Frame(self)
        self.header_frame.rowconfigure(0, weight=1)
        self.header_frame.columnconfigure(1, weight=1)

        self.header_frame.grid(row=0, padx=8, pady=8)

        self.header_frame.grid(row=0, sticky="news", padx=8, pady=8, columnspan=2)

        if self._deck:
            self.deck_title = ttk.Label(
                self.header_frame,
                text=self._deck.name,
                font=("Lato", 24, "bold"),
            )
            self.deck_title.grid(row=0, column=0, padx=8, pady=8)

            self.deck_title.bind("<Double-Button-1>", self._show_edit_deck_name_entry)
        else:
            self.deck_name_entry = ttk.Entry(
                self.header_frame, font=("Lato", 24, "bold")
            )
            self.deck_name_entry.grid(row=0, column=0, padx=8, pady=8)
            self.deck_name_entry.bind("<FocusOut>", self.save_deck)
            # self.deck_name_entry.bind("<Return>", self.save_deck)

        delete_button = ttk.Button(
            self.header_frame,
            text="Supprimer",
            style="Danger.TButton",
            command=lambda: self.delete_deck(self._deck),
        )
        delete_button.grid(row=0, column=2, sticky="e", padx=8, pady=8)

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

        if self._deck:
            for card in self._deck.cards:
                self.tree.insert(
                    "",
                    "end",
                    values=[card.question, card.answer],
                    iid=card.iid,
                )

        self.tree.bind("<<TreeviewSelect>>", self._item_selected)
        self.tree.grid(row=0, column=0, sticky="news")

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
        )
        self.answer_text.grid(column=0, row=19, padx=8, pady=8)

        buttons_group = ttk.Frame(right_column)
        buttons_group.grid(row=2, sticky="e")

        delete_card_button = ttk.Button(
            buttons_group,
            text="Supprimer",
            style="Danger.TButton",
            command=lambda: self.delete_card(self._current_card),
        )
        delete_card_button.grid(row=0, column=0, padx=8, pady=8, sticky="w")

        update_card_button = ttk.Button(
            buttons_group,
            text="Valider",
            style="Success.TButton",
            command=lambda: self.save_card(self._current_card),
        )
        update_card_button.grid(row=0, column=1, padx=8, pady=8, sticky="e")

    def save_card(self, card):
        if not card:
            self.add_card()
        else:
            self.update_card(card)
            self._current_card = None

    def _item_selected(self, event):
        for selected_item in self.tree.selection():
            card = self._deck.get_card_by_iid(selected_item)
            self._current_card = card
            self.edit_card(card)

    def edit_card(self, card):
        self.question_text.insert("1.0", card.question)
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

    def delete_card(self, card):
        self._app.database.delete_card(card.iid)
        deck = self._app.decks.get_deck_by_iid(card.iid)
        card = deck.get_card_by_iid(card.iid)
        deck.cards.remove(card)
        self.tree.delete(f"{card.iid}")
        self._app.events.notify("DELETE_CARD", "menu_decks_treeview", deck)
        self.question_text.delete("1.0", "end")
        self.answer_text.delete("1.0", "end")

    def add_card(self):
        question = self.question_text.get("1.0", "end").strip()  # type: ignore
        answer = self.answer_text.get("1.0", "end").strip()  # type: ignore
        if not question:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        if not answer:
            return messagebox.showerror("Erreur", 'Le champ "Réponse" est vide.')
        card = self._app.database.add_card(
            deck_id=self._deck.iid, question=question, answer=answer
        )
        self.tree.insert(
            "",
            "end",
            values=[card.question, card.answer],
            iid=card.iid,
        )
        self._deck.cards.append(card)
        self._app.events.notify("ADD_CARD", "menu_decks_treeview", self._deck)
        self.question_text.delete("1.0", "end")
        self.answer_text.delete("1.0", "end")

    def _show_edit_deck_name_entry(self, event):
        self.deck_title.destroy()
        self.deck_name_entry = ttk.Entry(self.header_frame, font=("Lato", 24, "bold"))
        self.deck_name_entry.grid(row=0, column=0, padx=8, pady=8)
        self.deck_name_entry.insert("0", self._deck.name)
        self.deck_name_entry.bind("<FocusOut>", self.on_focus_out)
        self.deck_name_entry.bind("<Return>", self.on_focus_out)

    def on_focus_out(self, event):
        deck_name = self.deck_name_entry.get()
        self._deck.name = deck_name
        self.deck_name_entry.destroy()
        if not deck_name:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        deck = self._app.database.update_deck(self._deck.iid, deck_name)

        self.deck_title = ttk.Label(
            self.header_frame,
            text=self._deck.name,
            font=("Lato", 24, "bold"),
        )
        self.deck_title.grid(row=0, column=0, padx=8, pady=8)

        self.deck_title.bind("<Double-Button-1>", self._show_edit_deck_name_entry)

    def delete_deck(self, deck):
        iid = deck.iid
        self._app.database.delete_deck(iid)
        self._app.decks.remove_deck(iid)
        self._app.events.notify("DELETE_DECK", "menu_decks_treeview", iid)
        self.destroy()

    def save_deck(self, event):
        deck_name = self.deck_name_entry.get()
        deck = self._app.database.create_deck(deck_name)
        self._deck = deck
        self._app.events.notify("ADD_DECK", "menu_decks_treeview", deck)
        self._app.decks.append(deck)
        self.deck_name_entry.destroy()
        self.deck_title = ttk.Label(
            self.header_frame,
            text=self._deck.name,
            font=("Lato", 24, "bold"),
        )
        self.deck_title.grid(row=0, column=0, padx=8, pady=8)

        self.deck_title.bind("<Double-Button-1>", self._show_edit_deck_name_entry)
