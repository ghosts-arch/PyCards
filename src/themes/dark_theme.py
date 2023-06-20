dark_theme = {
    ".": {
        "configure": {"background": "#2d2d2d", "foreground": "#F5F5F5", "font": "Lato"}
    },
    "TButton": {
        "configure": {
            "background": "#2196F3",
            "padding": [8, 8, 8, 8],
            "borderwidth": 0,
            "relief": "flat",
        },
        "map": {
            "background": [("active", "#1976D2"), ("disabled", "#4DD0E1")],
        },
    },
    "TEntry": {"configure": {"fieldbackground": "#4d4d4d"}},
    "Danger.TButton": {
        "configure": {"background": "#F44336"},
        "map": {
            "background": [("active", "#D32F2F"), ("disabled", "#E57373")],
        },
    },
    "Navbar.TFrame": {"configure": {"background": "#2d2d2d"}},
    "Default.TButton": {
        "configure": {"background": "#9E9E9E"},
        "map": {
            "background": [("active", "#616161")],
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
    "Success.TButton": {
        "configure": {"background": "#4CAF50"},
        "map": {
            "background": [("active", "#689F38"), ("disabled", "#81C784")],
        },
    },
}
