from bus_app.entity_models.purchase import Purchase
from bus_app.sql.create_tables import CREATE_PURCHASE_TABLE
from bus_app.sql.insert_tables import INSERT_PURCHASE


class PurchaseHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_PURCHASE_TABLE)

    def add_purchase(self, purchase: Purchase):
        with self.connection:
            self.cursor.execute(
                INSERT_PURCHASE,
                (purchase.purchase_date, purchase.purchased_balance, purchase.card_id),
            )
