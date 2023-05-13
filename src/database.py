from sqlalchemy import create_engine, delete, select, insert, update
from sqlalchemy.orm import Session

from .models import Base, Card


DATABASE_URL = "sqlite:///database.db"


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.connect = self.engine.connect()
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def init_demo(self):
        self.add_card({"question": "question 1", "answer": "answer 1"})
        self.add_card({"question": "question 2", "answer": "answer 2"})
        self.add_card({"question": "question 3", "answer": "answer 3"})
        self.session.commit()

    def add_card(self, data):
        query = (
            insert(Card)
            .values(question=data["question"], answer=data["answer"])
            .returning(Card)
        )
        result = self.connect.execute(query).first()
        self.connect.commit()
        return result._asdict()

    def update_card(self, iid, data):
        query = update(Card).where(Card.id == int(iid)).values(data).returning(Card)
        result = self.connect.execute(query).first()
        self.connect.commit()
        print(result._asdict())
        return result._asdict()

    def delete_card(self, id):
        query = delete(Card).where(Card.id == id)
        self.connect.execute(query)
        self.connect.commit()

    def get_cards(self):
        query = select(Card)
        result = self.connect.execute(query).all()
        return [record._asdict() for record in result]
