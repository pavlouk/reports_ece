from datetime import datetime
from bus_app.entity_models.itinerary import Itinerary
from bus_app.sql.create_tables import CREATE_BUS_TABLE
from bus_app.sql.insert_tables import INSERT_BUS


class BusHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_BUS_TABLE)

    ##itinerary functions
    def add_bus(self, bus):
        with self.connection:
            self.cursor.execute(INSERT_BUS, (bus,),)

    def delete_itinerary(self, itinerary_id: int):
        with self.connection:
            self.cursor.execute(f"DELETE from itinerary WHERE id={itinerary_id}")

    def set_bus_status(self, bus_id: int):
        with self.connection:
            self.cursor.execute(
                f"UPDATE itinerary SET 'ending_time'='{str(datetime.now())}' WHERE 'id'='{itinerary_id}'"
            )
