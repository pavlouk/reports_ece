import sqlite3
from datetime import datetime
from bus_app.entity_models.card import card
from bus_app.sql.create_tables import CREATE_CATEGORY_TABLE
from bus_app.sql.insert_tables import INSERT_CATEGORY


class CategoryHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_CATEGORY_TABLE)

    def add_card(self, name, category):
        with self.connection:
            self.cursor.execute(INSERT_CATEGORY, (name, category))
