from tkinter.ttk import Frame, Label, Treeview, Scrollbar, Button

from .add_card_window import AddCardWindow


class CardsManagement(Frame):
    def __init__(self, container):
        super().__init__(container)

        print(container)
        collection_size_string = f"Nombre de cartes - {len(container.master.questions)}"
        cards_collection_size_lbl = Label(self, text=collection_size_string)
        cards_collection_size_lbl.grid(row=0, padx=8, pady=8)

        tree = Treeview(
            self,
            columns=("question", "answer", "created_at"),
            show="headings",
        )
        tree.heading("question", text="Question", anchor="w")
        tree.heading("answer", text="Reponse", anchor="w")
        tree.heading("created_at", text="Rajoutée le", anchor="w")

        tree.grid(row=1, sticky="ew", padx=(8, 0), pady=8)

        scrollbar = Scrollbar(self, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky="ns", padx=(0, 8))

        for question in container.master.questions:
            tree.insert(
                "",
                "end",
                values=[
                    question.get("question"),
                    question.get("answer"),
                    question.get("created_at"),
                ],
            )
        create_card_btn = Button(
            self, text="Ajouter", command=self.show_create_card_window
        )

        create_card_btn.grid(row=2, padx=8, pady=8)

    def show_create_card_window(self):
        AddCardWindow(self)

    def update_cards_list(self, cards):
        notebook = self.children.get("!notebook")
        cards_management_tab = notebook.children.get("!frame2")
        lbl = cards_management_tab.children.get("!label")
        tree = cards_management_tab.children.get("!treeview")
        self.questions.append(cards)
        lbl["text"] = f"Nombre de cartes - {len(self.questions)}"
        for card in cards:
            tree.insert(
                "",
                "end",
                values=[
                    card.get("question"),
                    card.get("answer"),
                    card.get("created_at"),
                ],
            )
