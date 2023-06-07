from models.Card import Card


class Deck:
    def __init__(self, iid, name) -> None:
        self.iid = str(iid)
        self.name = name
        self.cards: list[Card] = []
