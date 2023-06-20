from tkinter import messagebox, ttk

from ..models.card import Card


from ..models.model import Model
from ..views.view import View


class EditorController:
    def __init__(self, model: Model, view: View, deck) -> None:
        self.model = model
        self.view = view
        self.current_deck = deck
        self.current_card = None
        self.frame = self.view.frames["Editor"]
        self.bind()

    def bind(self):
        if self.current_deck:
            self.deck_title = ttk.Label(
                self.frame.header_frame,
                text=self.current_deck.name,
                font=("Lato", 16, "bold"),
            )
            self.deck_title.grid(row=0, column=1, padx=8, pady=8, sticky="w")
            self.deck_title.bind("<Double-Button-1>", self._show_edit_deck_name_entry)
            for card in self.current_deck.cards:
                self.frame.tree.insert(
                    "",
                    "end",
                    values=[card.question, card.answer],
                    iid=card.iid,
                )
        else:
            self.deck_name_entry = ttk.Entry(
                self.frame.header_frame, font=("Lato", 16, "bold")
            )
            self.deck_name_entry.grid(row=0, column=1, padx=8, pady=8, sticky="w")
            self.deck_name_entry.bind("<Return>", self.save_deck)
            self.deck_name_entry.bind("<FocusOut>", self.save_deck)
        self.frame.tree.bind("<<TreeviewSelect>>", self._item_selected)
        self.frame.to_menu_button.config(command=self.back_to_home)
        self.frame.delete_deck_button.config(
            command=lambda: self.delete_deck(self.current_deck)
        )
        self.frame.delete_card_button.config(
            command=lambda: self.delete_card(self.current_card)
        )
        self.frame.update_card_button.config(command=self.add_card)

    def back_to_home(self):
        self.view.to("Home")

    def save_deck(self, event):
        deck_name = self.deck_name_entry.get()
        deck = self.model.decks.create_deck(deck_name)
        self.deck_name_entry.destroy()
        self.deck_title = ttk.Label(
            self.frame.header_frame,
            text=deck.name,
            font=("Lato", 16, "bold"),
        )
        self.deck_title.grid(row=0, column=1, padx=8, pady=8, sticky="w")
        self.current_deck = deck

    def _item_selected(self, event):
        for selected_item in self.frame.tree.selection():
            card = self.current_deck.get_card_by_iid(selected_item)
            self.current_card = card
            self.edit_card(card)

    def delete_card(self, card):
        self.current_deck.cards.remove(card)
        card = self.model.database.delete_card(card.iid)
        self.frame.tree.delete(f"{card.iid}")
        # self._app.events.notify("DELETE_CARD", "menu_decks_treeview", deck)
        self.frame.question_text.delete("1.0", "end")
        self.frame.answer_text.delete("1.0", "end")

    def save_card(self, card):
        if not card:
            self.add_card()
        else:
            self.update_card(card)
            self._current_card = None

    def edit_card(self, card):
        self.frame.question_text.insert("1.0", card.question)
        self.frame.answer_text.insert("1.0", card.answer)

    def update_card(self, card):
        question = self.frame.question_text.get("1.0", "end").strip()
        answer = self.frame.answer_text.get("1.0", "end").strip()
        if not question:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        if not answer:
            return messagebox.showerror("Erreur", 'Le champ "Réponse" est vide.')
        # card = self._app.database.update_card(card.iid, question, answer)
        self.frame.tree.item(card.iid, values=[card.question, card.answer])
        self.frame.question_text.delete("1.0", "end")
        self.frame.answer_text.delete("1.0", "end")

    def add_card(self):
        question = self.frame.question_text.get("1.0", "end").strip()  # type: ignore
        answer = self.frame.answer_text.get("1.0", "end").strip()  # type: ignore
        if not question:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        if not answer:
            return messagebox.showerror("Erreur", 'Le champ "Réponse" est vide.')

        card = self.model.database.add_card(
            deck_id=self.current_deck.iid, question=question, answer=answer
        )
        self.current_deck.add_card(card)

        self.frame.tree.insert(
            "",
            "end",
            values=[card.question, card.answer],
            iid=card.iid,
        )

        self.frame.question_text.delete("1.0", "end")
        self.frame.answer_text.delete("1.0", "end")

    def _show_edit_deck_name_entry(self, event):
        self.deck_title.destroy()
        self.deck_name_entry = ttk.Entry(
            self.frame.header_frame, font=("Lato", 16, "bold")
        )
        self.deck_name_entry.grid(row=0, column=0, padx=8, pady=8)
        self.deck_name_entry.insert("0", self.current_deck.name)
        self.deck_name_entry.bind("<FocusOut>", self.on_focus_out)
        self.deck_name_entry.bind("<Return>", self.on_focus_out)

    def on_focus_out(self, event):
        deck_name = self.deck_name_entry.get()
        self.current_deck.name = deck_name
        self.deck_name_entry.destroy()
        if not deck_name:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        # deck = self._app.database.update_deck(self._deck.iid, deck_name)

        self.deck_title = ttk.Label(
            self.frame.header_frame,
            text=self.current_deck.name,
            font=("Lato", 16, "bold"),
        )
        self.deck_title.grid(row=0, column=1, padx=8, pady=8)

        self.deck_title.bind("<Double-Button-1>", self._show_edit_deck_name_entry)

    def delete_deck(self, deck):
        iid = deck.iid
        self.model.decks.remove_deck(iid)
        self.view.to("Home")
