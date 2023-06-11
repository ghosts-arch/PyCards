class Deck:
    def __init__(self, iid, name) -> None:
        super().__init__()
        self._iid = str(iid)
        self._name = name
        self._cards = []

    @property
    def iid(self):
        return self._iid

    @property
    def name(self):
        return self._name

    @property
    def cards(self):
        return self._cards

    @name.setter
    def name(self, value):
        self._name = value

    @cards.setter
    def cards(self, value):
        self._cards = value

    def __repr__(self) -> str:
        return f"{self.iid}"
