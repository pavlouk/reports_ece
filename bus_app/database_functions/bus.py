from bus_app.entity_models.bus import Bus
from bus_app.sql.create_tables import CREATE_BUS_TABLE
from bus_app.sql.insert_tables import INSERT_BUS
from bus_app.sql.update_tables import UPDATE_BUS_STATUS_BY_ID

class BusHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_BUS_TABLE)

    def add_bus(self, bus: Bus):
        with self.connection:
            self.cursor.execute(INSERT_BUS, (bus.status, bus.capacity),)

    def set_status(self, bus_id: int, status: str):
        with self.connection:
            self.cursor.execute(UPDATE_BUS_STATUS_BY_ID, (bus_id, status))