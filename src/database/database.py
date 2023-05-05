from sqlalchemy import create_engine, text, select
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
        # self.session.execute(text("DROP TABLE IF EXISTS card"))
        # cards = Table(
        #    "cards",
        #    self.metadata,
        #   Column("id", Integer, autoincrement=True, primary_key=True),
        #    Column("question", Text),
        #    Column("answer", Text),
        # )
        # self.session.execute(text("create table cards (question text, answer text)"))
        self.session.execute(
            text("INSERT INTO cards (question, answer) VALUES (:question, :answer)"),
            [
                {"question": "test", "answer": "this is a test"},
                {"question": "test 2", "answer": "this is a test 2 "},
            ],
        )
        self.session.commit()
        # self.add_card({"question": "test", "answer": "test answers"})

    def add_card(self, data):
        card = Card(question=data["question"], answer=data["answer"])
        self.session.add(card)
        self.session.commit()

    def get_cards(self):
        query = select(Card)
        result = self.session.execute(query).all()
        return result
