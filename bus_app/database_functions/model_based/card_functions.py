from bus_app.sql.create_tables import CREATE_CARD_TABLE
from bus_app.sql.insert_tables import INSERT_CARD
from bus_app.sql.select_tables import SELECT_CARD_INFO
from bus_app.sql.update_tables import UPDATE_CARD_BALANCE_BY_ID
from bus_app.entity_models.card import Card


class CardHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_CARD_TABLE)

    def add_card(self, card: Card):
        with self.connection:
            self.cursor.execute(
                INSERT_CARD, (card.passenger_name, card.category_name, card.signup_date)
            )

    def get_card(self, card_id):
        with self.connection:
            return self.cursor.execute(SELECT_CARD_INFO, (card_id,)).fetchall()

    def update_balance(self, card_id, balance):
        with self.connection:
            self.cursor.execute(UPDATE_CARD_BALANCE_BY_ID, (balance, card_id))
