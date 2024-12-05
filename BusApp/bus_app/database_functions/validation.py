from bus_app.sql.create_tables import CREATE_VALIDATION_TABLE
from bus_app.sql.insert_tables import INSERT_VALIDATION
from bus_app.sql.select_tables import SELECT_VALIDATION_TIME
from bus_app.entity_models.validation import Validation


class ValidationHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_VALIDATION_TABLE)

    def add_validation(self, validation: Validation):
        with self.connection:
            self.cursor.execute(
                INSERT_VALIDATION,
                (
                    validation.card_id,
                    validation.itinerary_id,
                    validation.embarkation_time,
                ),
            )

    def get_embarkation_time(self, card_id: int, itinerary_id: int):
        with self.connection:
            return self.cursor.execute(
                SELECT_VALIDATION_TIME, (card_id, itinerary_id)
            ).fetchall()
