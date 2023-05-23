from sqlalchemy import create_engine, delete, select, insert, update
from sqlalchemy.orm import Session

from .models import Base, CardShema
from .core.Card import Card

DATABASE_URL = "sqlite:///database.db"


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.connect = self.engine.connect()
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def add_card(self, data):
        query = (
            insert(CardShema)
            .values(question=data["question"], answer=data["answer"])
            .returning(CardShema)
        )
        result = self.connect.execute(query).first()
        self.connect.commit()
        return Card.from_shema(result)

    def update_card(self, iid, data):
        query = (
            update(CardShema)
            .where(CardShema.id == int(iid))
            .values(data)
            .returning(CardShema)
        )
        result = self.connect.execute(query).first()
        self.connect.commit()
        return Card.from_shema(result)

    def delete_card(self, id):
        query = delete(CardShema).where(CardShema.id == id)
        self.connect.execute(query)
        self.connect.commit()

    def get_cards(self):
        query = select(CardShema)
        result = self.connect.execute(query).all()
        return [Card.from_shema(r) for r in result]
