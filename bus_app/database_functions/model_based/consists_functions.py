from bus_app.entity_models.consists import Consists
from bus_app.sql.create_tables import CREATE_CONSISTS_TABLE
from bus_app.sql.insert_tables import INSERT_CONSISTS


class ConsistsHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_CONSISTS_TABLE)

    def add_consists(self, consists: Consists):
        with self.connection:
            self.cursor.execute(
                INSERT_CONSISTS,
                (
                    consists.stop_id,
                    consists.route_name,
                    consists.stop_position,
                    consists.est_next_stop_toa,
                ),
            )
