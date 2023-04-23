import tkinter as tk
from add_card_window import AddCardWindow
from play_cards_windows import PlayCardsWindow


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.questions = []
        self.title("PyCards")
        self.state("zoomed")

        title = tk.Label(self, text="PyCards", font=("Arial", 24))
        title.pack(pady=20)
        buttons_frame = tk.Frame(self)
        buttons_frame.pack()
        create_card_btn = tk.Button(buttons_frame,
                                    text="Ajouter",
                                    command=self.show_create_card_window)
        start_btn = tk.Button(buttons_frame, text="Demarrer",
                              command=self.show_play_cards_window)

        create_card_btn.pack(side=tk.LEFT)
        start_btn.pack()

        collection_size_string = f"Nombre de cartes - {len(self.questions)}"
        cards_collection_size_lbl = tk.Label(self, text=collection_size_string)
        cards_collection_size_lbl.pack()

    def show_create_card_window(self):
        AddCardWindow(self)

    def show_play_cards_window(self):
        PlayCardsWindow(self)

    def update_cards_list(self):
        lbl = self.children.get("!label2")
        lbl["text"] = f"Nombre de cartes - {len(self.questions)}"
