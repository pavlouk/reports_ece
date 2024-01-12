from datetime import datetime
from bus_app.entity_models.itinerary import Itinerary
from bus_app.sql.create_tables import CREATE_ITINERARY_TABLE
from bus_app.sql.insert_tables import INSERT_ITINERARY


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

    def get_all_itineraries(self):
        self.cursor.execute("SELECT * from itinerary")
        results = self.cursor.fetchall()

        itinerarys = []
        for result in results:
            itinerarys.append(result)

        return itinerarys


    def set_ending_time(self, itinerary_id: int):
        with self.connection:
            self.cursor.execute(
                f"UPDATE itinerary SET 'ending_time'='{str(datetime.now())}' WHERE 'id'='{itinerary_id}'"
            )
