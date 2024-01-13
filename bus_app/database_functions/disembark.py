from bus_app.sql.create_tables import CREATE_CARD_BALANCE_CHARGE_TRIGGER_ON_DISEMBARKATION, CREATE_DISEMBARKATION_TABLE
from bus_app.sql.insert_tables import INSERT_DISEMBARKATION
from bus_app.entity_models.disembark import Disembark


class DisembarkHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_DISEMBARKATION_TABLE)
        self.cursor.executescript(CREATE_CARD_BALANCE_CHARGE_TRIGGER_ON_DISEMBARKATION)

    def add_disembark(self, disembark: Disembark):
        print(disembark.card_id, disembark.itinerary_id, disembark.charge_id)
        with self.connection:
            self.cursor.execute(INSERT_DISEMBARKATION,
                (
                    disembark.card_id,
                    disembark.itinerary_id,
                    disembark.charge_id,
                ),
            )
