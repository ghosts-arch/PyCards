import sqlalchemy
from sqlalchemy.orm import Session
from .models.base import Base
from .models.card import Card


class Database:
    def __init__(self):
        self.engine = sqlalchemy.create_engine(
            "sqlite:///database.db", echo=True)
        self.connect = self.engine.connect()
        self.metadata = Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def add_card(self, card):
        pass

    def get_cards(self):
        query = sqlalchemy.select(Card)
        result = self.connect.execute(query).all()
        return result
