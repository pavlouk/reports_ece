from bus_app.entity_models.charge import Charge
from bus_app.sql.create_tables import CREATE_CHARGE_TABLE
from bus_app.sql.insert_tables import INSERT_CHARGE


class ChargeHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_CHARGE_TABLE)

    def add_charge(self, charge: Charge):
        with self.connection:
            self.cursor.execute(
                INSERT_CHARGE, (charge.disembark_time, charge.amount_charged)
            )
