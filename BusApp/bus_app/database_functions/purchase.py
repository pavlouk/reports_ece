from bus_app.entity_models.purchase import Purchase
from bus_app.sql.create_tables import CREATE_PURCHASE_TABLE, CREATE_CARD_BALANCE_FILLUP_ON_PURCHASE_TRIGGER
from bus_app.sql.insert_tables import INSERT_PURCHASE
from bus_app.sql.select_tables import SELECT_COMPANY_EARNINGS, SELECT_TOTAL_COMPANY_EARNINGS


class PurchaseHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_PURCHASE_TABLE)
        self.cursor.executescript(CREATE_CARD_BALANCE_FILLUP_ON_PURCHASE_TRIGGER)

    def add_purchase(self, purchase: Purchase):
        with self.connection:
            self.cursor.execute(
                INSERT_PURCHASE,
                (purchase.purchase_date, purchase.purchased_balance, purchase.card_id),
            )

    def get_earnings(self, start_date: str, end_date: int):
        with self.connection:
            return self.cursor.execute(SELECT_COMPANY_EARNINGS, (start_date, end_date)).fetchall()

    def get_all_earnings(self):
        with self.connection:
            return self.cursor.execute(SELECT_TOTAL_COMPANY_EARNINGS).fetchall()
      