from tkinter import Toplevel, Text, messagebox
from tkinter.ttk import Label, Button, Frame, Entry


class EditDeckWindow(Toplevel):
    def __init__(self, master, deck):
        super().__init__(background="#2d2d2d")

        print(deck)
        self.master = master
        self.deck = deck

        self.resizable(False, False)
        self.grab_set()

        title = Label(self, text="Editer un paquet")
        title.grid(row=0, column=0, padx=8, pady=8)

        input_field = Frame(self)
        input_field.grid(row=1, padx=8, pady=8)

        deck_name = Label(input_field, text="Nom")
        deck_name.grid(row=1, padx=(8, 4), pady=8)

        self.deck_name_entry = Entry(input_field)
        self.deck_name_entry.insert(0, self.deck["name"])
        self.deck_name_entry.grid(row=1, column=1, padx=(4, 8), pady=8)

        buttons_group = Frame(self)
        buttons_group.grid(row=3, sticky="e")
        add_card_btn = Button(
            buttons_group,
            text="Supprimer",
            command=self.delete_card,
            style="Danger.TButton",
        )
        add_card_btn.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        add_card_btn = Button(
            buttons_group,
            text="Valider",
            command=self.update_deck,
            style="Success.TButton",
        )
        add_card_btn.grid(row=0, column=1, padx=8, pady=8)

    def update_deck(self):
        deck_name = self.deck_name_entry.get().strip()  # type: ignore
        if not deck_name:
            return messagebox.showerror("Erreur", 'Le champ "Question" est vide.')
        iid = self.deck.get("id")
        self.master.update_deck(iid, {"name": deck_name})  # type: ignore
        self.deck_name_entry.delete(0, "end")

    def delete_card(self):
        iid = self.deck.get("id")
        self.master.delete_deck(iid)
        self.destroy()
