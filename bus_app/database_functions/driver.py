from bus_app.entity_models.driver import Driver
from bus_app.sql.create_tables import CREATE_DRIVER_TABLE
from bus_app.sql.insert_tables import INSERT_DRIVER
from bus_app.sql.update_tables import UPDATE_DRIVER_AVAILABILITY_BY_ID


class DriverHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_DRIVER_TABLE)

    def add_driver(self, driver: Driver):
        with self.connection:
            self.cursor.execute(
                INSERT_DRIVER, (driver.hired_date, driver.availiability, driver.name)
            )

    def set_status(self, driver_id: int, availiability: str):
        with self.connection:
            self.cursor.execute(
                UPDATE_DRIVER_AVAILABILITY_BY_ID, (driver_id, availiability)
            )
