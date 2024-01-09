from bus_app.sql.create_tables import CREATE_VALIDATION_TABLE
from bus_app.sql.insert_tables import INSERT_VALIDATION
from datetime import datetime

class ValidateHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_VALIDATION_TABLE)

    def add_validation(self, card_id, itinerary_id):
        with self.connection:
            self.cursor.execute(INSERT_VALIDATION, (datetime.utcnow(), tickets, pay, card_id, category_id))
