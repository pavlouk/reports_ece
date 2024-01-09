from bus_app.sql.create_tables import CREATE_VALIDATION_TABLE
from bus_app.sql.insert_tables import INSERT_VALIDATION
from datetime import datetime


class ValidationHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_VALIDATION_TABLE)

    def validate_ticket(
        self, card_id, itinerary_id, embarkation_time=None, disembarkation_time=None
    ):
        with self.connection:
            self.cursor.execute(
                INSERT_VALIDATION,
                (
                    card_id,
                    itinerary_id,
                    embarkation_time or datetime.utcnow(),
                    disembarkation_time,
                ),
            )
