import sqlite3
from datetime import datetime
from bus_app.entity_models.card import Card
from bus_app.sql.create_tables import CREATE_CARD_TABLE
from bus_app.sql.insert_tables import INSERT_CARD


class CardHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_CARD_TABLE)

    def add_card(self, name, category):
        with self.connection:
            self.cursor.execute(INSERT_CARD, (name, category))
