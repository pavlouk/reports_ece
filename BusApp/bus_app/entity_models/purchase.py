from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")

MAX_CARDS = 100

class Purchase:
    def __init__(self, card_id=None, purchased_balance=None, purchase_date=None):
        self.card_id = card_id or fake.random_int(min=1, max=MAX_CARDS)
        self.purchased_balance = purchased_balance or float(fake.random_int(min=1, max=MAX_CARDS) / 10.0)
        self.purchase_date = purchase_date or fake.date_between(start_date="-1y")



