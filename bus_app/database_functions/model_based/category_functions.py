import sqlite3
from datetime import datetime
from bus_app.entity_models.card import Card
from bus_app.sql.create_tables import CREATE_CATEGORY_TABLE
from bus_app.sql.insert_tables import INSERT_CATEGORY


class CategoryHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_CATEGORY_TABLE)

    def add_category(self, name, discount):
        with self.connection:
            self.cursor.execute(INSERT_CATEGORY, (name, discount))
