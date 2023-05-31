import sqlite3


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
                FOREIGN KEY (deck_id) REFERENCES deck(id)
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
            return result
        except sqlite3.Error as err:
            raise sqlite3.Error(err)

    def get_card(self, id):
        try:
            query = "SELECT * FROM card WHERE card.id = ?"
            result = self.cursor.execute(query, id).fetchone()
            return result
        except sqlite3.Error as err:
            raise sqlite3.Error(err)

    def add_card(self, card):
        try:
            query = "INSERT INTO card(question, answer, deck_id, created_at) VALUES (?,?,1,datetime('now')) RETURNING *"
            result = self.cursor.execute(
                query, (card["question"], card["answer"])
            ).fetchone()
            self.connection.commit()
            return result
        except sqlite3.Error as err:
            raise err

    def update_card(self, id, data):
        try:
            query = "UPDATE card SET question = ?, answer = ? WHERE id = ? RETURNING *"
            result = self.cursor.execute(
                query, (data["question"], data["answer"], id)
            ).fetchone()
            self.connection.commit()
            return result
        except sqlite3.Error as err:
            raise sqlite3.Error(err)

    def delete_card(self, id):
        try:
            query = "DELETE FROM card WHERE id = ? RETURNING *"
            result = self.cursor.execute(query, id).fetchone()
            self.connection.commit()
            return result
        except:
            pass

    def get_decks(self):
        query = "SELECT * FROM deck"
        result = self.cursor.execute(query).fetchall()
        return result

    def create_deck(self, name: str):
        try:
            query = "INSERT INTO deck(name) VALUES(?) RETURNING *"
            result = self.cursor.execute(query, (name,)).fetchone()
            self.connection.commit()
            return result
        except sqlite3.Error as err:
            raise err

    def init(self):
        self.create_decks_table()
        self.create_cards_table()
