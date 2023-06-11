from tkinter import Toplevel, Text, messagebox
from tkinter.ttk import Label, Button, Frame, Combobox


class AddCardWindow(Toplevel):
    def __init__(self, container):
        super().__init__(background="#2d2d2d")
        self.container = container
        self.resizable(False, False)
        self.grab_set()

        deck_label = Label(self, text="Paquet")
        self.combobox = Combobox(self, height=8, font=("Lato", 12), name="deck_select")
        self.combobox["values"] = [
            deck.name for deck in self.container.master.master.decks
        ]
        self.combobox.grid(row=1, padx=8, pady=8, sticky="news")
        deck_label.grid(row=0, sticky="w", padx=8, pady=8)

        question = Label(self, text="Question")
        question.grid(row=2, sticky="w", padx=8, pady=8)

        question_text = Text(
            self,
            name="question_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        question_text.grid(row=3, padx=8, pady=8)

        answer = Label(self, text="Reponse")
        answer.grid(row=4, padx=8, pady=8, sticky="w")

        answer_text = Text(
            self,
            name="answer_text",
            height=8,
            background="#4d4d4d",
            foreground="white",
            borderwidth=0,
            font=("Lato", 12),
        )
        answer_text.grid(row=5, padx=8, pady=8)

        buttons_group = Frame(self)
        buttons_group.grid(row=6, sticky="e")
        add_card_btn = Button(
            buttons_group,
            text="Annuler",
            command=self.close_window,
            style="Default.TButton",
        )
        add_card_btn.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        add_card_btn = Button(
            buttons_group,
            text="Ajouter",
            command=self.add_card,
            style="Success.TButton",
        )
        add_card_btn.grid(row=0, column=1, padx=8, pady=8)

    def close_window(self):
        self.destroy()

    def add_card(self):
        question_entry = self.children.get("question_text")
        answer_entry = self.children.get("answer_text")
        deck_select = self.children.get("deck_select")
        deck_name = deck_select.get()
        if not deck_name:
            return messagebox.showerror("Erreur", 'Le champ "Paquet" est vide.')
        deck = self.get_deck_by_name(deck_name=deck_name)
        if not deck:
            deck = self.container.master.master.database.create_deck(deck_name)
            self.container.tree.insert(
                "", "end", text=deck.name, iid=f"d-{deck.iid}", open=False
            )
            self.add_option(deck_name)
            self.container.app.events.notify("ADD_DECK", "menu_decks_treeview", deck)
            self.container.app.decks.append(deck)
        deck_id = deck.iid
        question = question_entry.get("1.0", "end").strip()  # type: ignore
        answer = answer_entry.get("1.0", "end").strip()  # type: ignore
        if not question:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        if not answer:
            return messagebox.showerror("Erreur", 'Le champ "Réponse" est vide.')
        self.container.add_card(deck_id, question, answer)  # type: ignore
        question_entry.delete("1.0", "end")
        answer_entry.delete("1.0", "end")
        deck_select.delete(0, "end")

    def get_deck_by_name(self, deck_name):
        for deck in self.container.master.master.decks:
            if deck.name == deck_name:
                return deck

    def add_option(self, option):
        values = self.combobox["values"]
        values_list = list(values)
        values_list.append(option)
        self.combobox["values"] = tuple(values_list)
