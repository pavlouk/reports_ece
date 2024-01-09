from bus_app.sql.create_tables import CREATE_CHARGE_TABLE
from bus_app.sql.insert_tables import INSERT_CHARGE


class ChargeHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_CHARGE_TABLE)

    def add_charge(self, card_id, category):
        with self.connection:
            self.cursor.execute(INSERT_CHARGE, (name, category))
