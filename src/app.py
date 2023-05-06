from tkinter import Tk, messagebox, W
from tkinter.ttk import Label, Button, Style, Treeview, Notebook, Frame, Scrollbar
from src.add_card_window import AddCardWindow
from src.play_cards_windows import PlayCardsWindow
from .database import Database
from .cards_management import CardsManagement


class App(Tk):
    def __init__(self):
        super().__init__()
        self.database = Database()
        # self.database.init_demo()
        self.questions = self.database.get_cards()
        self.title("PyCards")
        self.state("zoomed")
        self.configure(background="blue")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # styles

        s = Style()
        s.configure("TButton", font=("Lato", 12))
        s.configure("TLabel", font=("Lato", 12))
        s.configure("Treeview.Heading", font=("Lato", 12))
        s.configure("TNotebook.Tab", font=("Lato", 12), padding=[8, 8, 8, 8])
        s.configure(
            "TNotebook", tabposition="n", font=("Lato", 65), tabmargins=[8, 8, 8, 8]
        )

        notebook = Notebook(self)
        notebook.grid(row=0, column=0, sticky="news")

        main_menu = Frame(notebook)
        cards_management = CardsManagement(notebook)

        main_menu.grid()
        cards_management.grid()

        cards_management.columnconfigure(0, weight=1)
        main_menu.columnconfigure(0, weight=1)
        main_menu.rowconfigure(0, weight=1)

        notebook.add(main_menu, text="Menu Principal")
        notebook.add(cards_management, text="Gerer les cartes")

        start_btn = Button(
            main_menu, text="Demarrer", command=self.show_play_cards_window
        )

        start_btn.grid(row=0, padx=8, pady=8)

    def show_play_cards_window(self):
        if not len(self.questions):
            return messagebox.showerror("Erreur", "Aucune carte trouvée !")
        PlayCardsWindow(self)

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
