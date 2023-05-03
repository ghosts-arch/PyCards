import sqlalchemy
from sqlalchemy.orm import Session


class Database:
    def __init__(self):
        self.engine = sqlalchemy.create_engine(
            "sqlite:///database.db", echo=True)
        self.connect = self.engine.connect()
        self.metadata = sqlalchemy.MetaData()
        self.session = Session

    def create_tables(self):
        self.cards = sqlalchemy.Table(
            "cards",
            self.metadata,
            sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
            sqlalchemy.Column(
                'question', sqlalchemy.String(255), nullable=False),
            sqlalchemy.Column('answer', sqlalchemy.String(255), nullable=False))
        self.metadata.create_all(self.engine)
        print(self.metadata.tables)
        self.connect.execute(self.cards.insert().values(
            question="test", answer="test"))

    def get_cards(self):
        cards = []
        query = self.s
        result = self.connect.execute(query)
        for x in result:
            cards.append({
                "question": x[2]
            })
