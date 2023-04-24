from tkinter import Tk, messagebox
from tkinter.ttk import Label, Button, Style, Treeview, Notebook, Frame
from add_card_window import AddCardWindow
from play_cards_windows import PlayCardsWindow


class App(Tk):
    def __init__(self):
        super().__init__()
        self.questions = []
        self.title("PyCards")
        self.state("zoomed")

        # styles

        s = Style()
        s.configure("TButton", font=("Lato", 16))
        # s.configure("TNotebook", tabposition="n")

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
            cards_management, text=collection_size_string, font=("Helvetica", 12))
        cards_collection_size_lbl.pack()

        tree = Treeview(cards_management, columns=("question", "answer"),
                        show='headings')
        tree.heading('question', text="Question")
        tree.heading("answer", text='Reponse')

        tree.pack()

        create_card_btn = Button(cards_management,
                                 text="Ajouter",
                                 command=self.show_create_card_window)

        start_btn = Button(main_menu, text="Demarrer",
                           command=self.show_play_cards_window)

        create_card_btn.pack()
        start_btn.pack(padx=8, pady=8)

    def show_create_card_window(self):
        AddCardWindow(self)

    def show_play_cards_window(self):
        if not len(self.questions):
            return messagebox.showerror("Erreur", 'Aucune carte trouvée !')
        PlayCardsWindow(self)

    def update_cards_list(self):
        lbl = self.children.get("!label2")
        lbl["text"] = f"Nombre de cartes - {len(self.questions)}"
