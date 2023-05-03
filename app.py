from tkinter import Tk, messagebox, W
from tkinter.ttk import Label, Button, Style, Treeview, Notebook, Frame
from add_card_window import AddCardWindow
from play_cards_windows import PlayCardsWindow
from database import Database


class App(Tk):
    def __init__(self):
        super().__init__()
        self.database = Database()
        self.database.create_tables()
        self.questions = self.database.get_cards()
        print(self.questions)
        self.title("PyCards")
        self.state("zoomed")
        self.configure(background="blue")

        # styles

        s = Style()
        s.configure("TButton", font=("Lato", 12))
        s.configure("TLabel", font=("Lato", 12))
        s.configure("Treeview.Heading", font=("Lato", 12))
        s.configure("TNotebook.Tab", font=(
            "Lato", 12), padding=[8, 8, 8, 8])
        s.configure("TNotebook", tabposition="n", font=(
            "Lato", 65), tabmargins=[8, 8, 8, 8])

        notebook = Notebook(self)
        notebook.pack(fill='both', expand=True)

        main_menu = Frame(notebook)
        cards_management = Frame(notebook)

        main_menu.pack()
        cards_management.pack()

        notebook.add(main_menu, text="Menu Principal")
        notebook.add(cards_management, text="Gerer les cartes")

        # title = Label(main_menu, text="PyCards", font=(
        #    "Lato", 48), foreground='grey')
        # title.pack()

        collection_size_string = f"Nombre de cartes - {len(self.questions)}"
        cards_collection_size_lbl = Label(
            cards_management, text=collection_size_string)
        cards_collection_size_lbl.pack(padx=8, pady=8)

        tree = Treeview(cards_management, columns=("question", "answer", "created_at"),
                        show='headings')
        tree.heading('question', text="Question", anchor=W)
        tree.heading("answer", text='Reponse', anchor=W)
        tree.heading("created_at", text='Rajoutée le', anchor=W)

        tree.pack(padx=16, pady=8, fill="x")

        for question in self.questions:
            tree.insert("", "end", {"question": })
        create_card_btn = Button(cards_management,
                                 text="Ajouter",
                                 command=self.show_create_card_window)

        start_btn = Button(main_menu, text="Demarrer",
                           command=self.show_play_cards_window)

        create_card_btn.pack(padx=8, pady=8)
        start_btn.pack(padx=8, pady=8)

    def show_create_card_window(self):
        AddCardWindow(self)

    def show_play_cards_window(self):
        if not len(self.questions):
            return messagebox.showerror("Erreur", 'Aucune carte trouvée !')
        PlayCardsWindow(self)

    def update_cards_list(self):
        notebook = self.children.get('!notebook')
        cards_management_tab = notebook.children.get("!frame2")
        lbl = cards_management_tab.children.get("!label")
        lbl["text"] = f"Nombre de cartes - {len(self.questions)}"
