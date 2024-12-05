from bus_app.sql.create_tables import CREATE_CATEGORY_TABLE
from bus_app.sql.insert_tables import INSERT_CATEGORY
from bus_app.sql.select_tables import SELECT_CATEGORY_DISCOUNT, SELECT_CATEGORIES


class CategoryHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_CATEGORY_TABLE)

    def add_category(self, name, discount):
        with self.connection:
            self.cursor.execute(INSERT_CATEGORY, (name, discount))

    def get_discount(self, category_id):
        with self.connection:
            return self.cursor.execute(SELECT_CATEGORY_DISCOUNT, (category_id,)).fetchall()

    def get_categories(self):
        with self.connection:
            return self.cursor.execute(SELECT_CATEGORIES).fetchall()
