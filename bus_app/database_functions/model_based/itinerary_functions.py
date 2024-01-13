from datetime import datetime
from bus_app.entity_models.itinerary import Itinerary
from bus_app.sql.create_tables import CREATE_ITINERARY_TABLE
from bus_app.sql.insert_tables import INSERT_ITINERARY
from bus_app.sql.select_tables import SELECT_ITINERARIES
from bus_app.sql.update_tables import UPDATE_ITINERARY_BY_ID


class ItineraryHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_ITINERARY_TABLE)

    def add_itinerary(self, itinerary: Itinerary):
        with self.connection:
            self.cursor.execute(
                INSERT_ITINERARY,
                (
                    itinerary.starting_time,
                    itinerary.direction,
                    itinerary.route_name,
                    itinerary.bus_id,
                    itinerary.driver_id,
                ),
            )

    def get_itineraries(self):
        with self.connection:
            return self.cursor.execute(SELECT_ITINERARIES).fetchall()

    def set_ending_time(self, itinerary_id: int):
        with self.connection:
            self.cursor.execute(
                UPDATE_ITINERARY_BY_ID,
                (
                    itinerary_id,
                    datetime.utcnow(),
                ),
            )
