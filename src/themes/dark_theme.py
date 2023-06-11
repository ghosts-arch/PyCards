dark_theme = {
    ".": {
        "configure": {"background": "#2d2d2d", "foreground": "white", "font": "Lato"}
    },
    "TButton": {
        "configure": {
            "background": "blue",
            "padding": [8, 8, 8, 8],
            "borderwidth": 0,
            "relief": "flat",
        },
        "map": {
            "background": [("active", "darkblue"), ("disabled", "grey")],
        },
    },
    "TEntry": {"configure": {"fieldbackground": "#4d4d4d"}},
    "Danger.TButton": {
        "configure": {"background": "red"},
        "map": {
            "background": [
                ("active", "darkred"),
            ],
        },
    },
    "Success.TButton": {
        "configure": {"background": "green"},
        "map": {
            "background": [
                ("active", "darkgreen"),
            ],
        },
    },
    "Navbar.TFrame": {"configure": {"background": "#2d2d2d"}},
    "Default.TButton": {
        "configure": {"background": "grey"},
        "map": {
            "background": [("active", "darkgrey")],
        },
    },
    "TNotebook.Tab": {"map": {"background": [("selected", "blue")]}},
    "Treeview": {
        "configure": {
            "font": ("Lato", 16, "normal"),
            "padding": [8, 8, 8, 8],
            "background": "#2d2d2d",
            "rowheight": 32,
            "borderwidth": 0,
            "anchor": "w",
            "fieldbackground": "#2d2d2d",
        },
        "map": {"background": [("selected", "#6d6d6d")]},
    },
    "Treeview.treearea": {"configure": {"foreground": "red"}},
    "TSeparator": {"configure": {"background": "##4d4d4d"}},
    "TCombobox": {
        "configure": {
            "background": "#2d2d2d",  # Dark grey background
            "foreground": "white",  # White text
            "fieldbackground": "#4d4d4d",
            "insertcolor": "white",
            "bordercolor": "black",
            "lightcolor": "#4d4d4d",
            "darkcolor": "black",
            "arrowcolor": "white",
        },
    },
    "TLabel": {"configure": {"font": ("Lato", 12)}},
    "Treeview.Heading": {
        "configure": {
            "font": ("Lato", 12),
            "padding": [8, 8, 8, 8],
            "borderwidth": 0,
            "background": "#4d4d4d",
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "font": ("Lato", 12),
            "padding ": [8, 8, 8, 8],
            "borderwidth": 0,
        }
    },
    "TNotebook": {
        "configure": {
            "tabposition": "n",
            "font": ("Lato", 65),
            "tabmargins": [8, 8, 8, 8],
            "borderwidth": 0,
            "relief": "solid",
        }
    },
    "Default.TButton": {"configure": {"background": "grey"}},
    "Success.TButton": {"configure": {"background": "green"}},
}
