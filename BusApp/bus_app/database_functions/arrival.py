from bus_app.sql.create_tables import CREATE_ARRIVAL_TABLE
from bus_app.sql.insert_tables import INSERT_ARRIVAL
from bus_app.entity_models.arrival import Arrival


class ArrivalHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_ARRIVAL_TABLE)

    def add_arrival(self, arrival: Arrival):
        with self.connection:
            self.cursor.execute(INSERT_ARRIVAL,
                (
                    arrival.itinerary_id,
                    arrival.stop_id,
                    arrival.real_toa,
                ),
            )
