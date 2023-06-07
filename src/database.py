import sqlite3

from core.Deck import Deck

from .core.Card import Card


class Database:
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor

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
            raise err

    def create_cards_table(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS card ( 
                id INTEGER PRIMARY KEY, 
                question TEXT NOT NULL, 
                answer TEXT NOT NULL,
                deck_id INTEGER NOT NULL, 
                created_at TEXT,
                FOREIGN KEY (deck_id) 
                    REFERENCES deck(id) 
                    ON UPDATE SET NULL
                    ON DELETE SET NULL
            ) 
            """
            self.connection.execute(query)
        except sqlite3.Error as err:
            raise err

    def create_decks_table(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS deck (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            UNIQUE(name)
            )
            """
            self.cursor.execute(query)
        except:
            pass

    def get_cards(self):
        try:
            query = "SELECT * FROM card"
            result = self.cursor.execute(query).fetchall()
            return [
                Card(
                    iid=r["id"],
                    question=r["question"],
                    answer=r["answer"],
                    deck_id=r["deck_id"],
                    created_at=r["created_at"],
                )
                for r in result
            ]
        except sqlite3.Error as err:
            raise sqlite3.Error(err)

    def get_card(self, id):
        try:
            query = "SELECT * FROM card WHERE card.id = ?"
            result = self.cursor.execute(query, id).fetchone()
            return Card(
                iid=result["iid"],
                question=result["question"],
                answer=result["answer"],
                deck_id=result["deck_id"],
                created_at=result["created_at"],
            )
        except sqlite3.Error as err:
            raise sqlite3.Error(err)

    def add_card(self, deck_id, question, answer):
        try:
            query = "INSERT INTO card(question, answer, deck_id, created_at) VALUES (?,?,?,datetime('now')) RETURNING *"
            result = self.cursor.execute(query, (question, answer, deck_id)).fetchone()
            self.connection.commit()
            return Card(
                iid=result["iid"],
                question=result["question"],
                answer=result["answer"],
                deck_id=result["deck_id"],
                created_at=result["created_at"],
            )
        except sqlite3.Error as err:
            raise err

    def update_card(self, id, question, answer):
        try:
            query = "UPDATE card SET question = ?, answer = ? WHERE id = ? RETURNING *"
            result = self.cursor.execute(query, (question, answer, id)).fetchone()
            self.connection.commit()
            return Card(
                iid=result["iid"],
                question=result["question"],
                answer=result["answer"],
                deck_id=result["deck_id"],
                created_at=result["created_at"],
            )
        except sqlite3.Error as err:
            raise sqlite3.Error(err)

    def delete_card(self, id):
        try:
            query = "DELETE FROM card WHERE id = ? RETURNING *"
            result = self.cursor.execute(query, id).fetchone()
            self.connection.commit()
            return Card(
                iid=result["iid"],
                question=result["question"],
                answer=result["answer"],
                deck_id=result["deck_id"],
                created_at=result["created_at"],
            )
        except:
            pass

    def get_decks(self):
        query = "SELECT * FROM deck"
        result = self.cursor.execute(query).fetchall()
        return [Deck(iid=d["id"], name=d["name"]) for d in result]

    def create_deck(self, name: str):
        try:
            query = "INSERT INTO deck(name) VALUES(?) RETURNING *"
            result = self.cursor.execute(query, (name,)).fetchone()
            self.connection.commit()
            return Deck(iid=result["id"], name=result["name"])
        except sqlite3.Error as err:
            raise err

    def update_deck(self, id, name):
        try:
            query = "UPDATE deck SET name = ? WHERE id = ? RETURNING *"
            result = self.cursor.execute(query, (name, id)).fetchone()
            self.connection.commit()
            return Deck(iid=result["id"], name=result["name"])
        except sqlite3.Error as err:
            raise err

    def delete_deck(self, id):
        try:
            delete_deck_query = "DELETE FROM deck WHERE id = ? RETURNING *;"
            deck = self.cursor.executemany(delete_deck_query, str(id)).fetchone()
            delete_cards_query = "DELETE FROM card WHERE deck_id = ?;"
            self.cursor.execute(delete_cards_query, str(id))
            self.connection.commit()
            return deck
        except sqlite3.Error as err:
            raise err

    def init(self):
        self.create_decks_table()
        self.create_cards_table()
