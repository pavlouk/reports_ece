from bus_app.entity_models.stop import Stop
from bus_app.sql.create_tables import CREATE_STOP_TABLE
from bus_app.sql.insert_tables import INSERT_STOP
from bus_app.sql.select_tables import SELECT_STOP_INFO

class StopHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_STOP_TABLE)
        
    def add_stop(self, stop: Stop):
        with self.connection:
            self.cursor.execute(INSERT_STOP, (stop.name, stop.location))

    def get_stop(self, stop_id: int):
        with self.connection:
            return self.cursor.execute(SELECT_STOP_INFO, (stop_id)).fetchall()