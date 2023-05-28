"""
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
"""

import sqlite3
import datetime


class Database:
    connection: sqlite3.Connection

    # see https://stackoverflow.com/a/3300514
    def _as_dict(self, cursor, row):
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        return d

    def connect(self):
        try:
            self.connection = sqlite3.connect("./database.db")
            self.cursor = self.connection.cursor()
            self.cursor.row_factory = self._as_dict
        except sqlite3.Error as err:
            print(err)

    def create_cards_table(self):
        try:
            self.connection.execute(
                """
            CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            created_at TEXT
            )
            """
            )
        except sqlite3.Error as err:
            print(err)

    def get_cards(self):
        try:
            query = "SELECT * FROM cards"
            result = self.cursor.execute(query).fetchall()
            return result
        except sqlite3.Error as err:
            raise sqlite3.Error(err)

    def get_card(self, id):
        try:
            query = "SELECT * FROM cards WHERE card.id = ?"
            result = self.cursor.execute(query, id).fetchone()
            return result
        except sqlite3.Error as err:
            raise sqlite3.Error(err)

    def add_card(self, card):
        try:
            query = "INSERT INTO cards(question, answer, created_at) VALUES (?,?,datetime('now')) RETURNING *"
            result = self.cursor.execute(
                query, (card["question"], card["answer"])
            ).fetchone()
            self.connection.commit()
            return result
        except sqlite3.Error as err:
            print(err)

    def update_card(self, id, data):
        try:
            query = "UPDATE cards SET question = ?, answer = ? WHERE id = ? RETURNING *"
            result = self.cursor.execute(
                query, (data["question"], data["answer"], id)
            ).fetchone()
            self.connection.commit()
            return result
        except sqlite3.Error as err:
            raise sqlite3.Error(err)

    def delete_card(self, id):
        try:
            query = "DELETE FROM cards WHERE id = ? RETURNING *"
            result = self.cursor.execute(query, id).fetchone()
            self.connection.commit()
            return result
        except:
            pass

    def init(self):
        self.create_cards_table()
