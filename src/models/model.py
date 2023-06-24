from .database import Database
from .decks import Decks


class Model:
    def __init__(self) -> None:
        self.database = Database()
        self.decks = Decks(database=self.database)
