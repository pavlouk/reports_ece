from datetime import datetime
from bus_app.entity_models.stop import Stop
from bus_app.sql.create_tables import CREATE_STOP_TABLE
from bus_app.sql.insert_tables import INSERT_STOP

class StopHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_STOP_TABLE)
        
    def add_stop(self, name, location):
        with self.connection:
            self.execute(INSERT_STOP, (name, location))