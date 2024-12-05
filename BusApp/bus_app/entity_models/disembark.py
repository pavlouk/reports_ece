from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")

MAX_CARDS = 10


class Disembark:
    def __init__(
        self,
        card_id=None,
        itinerary_id=None,
        charge_id=None,
    ):
        self.card_id = card_id or fake.random_int(min=1, max=MAX_CARDS)
        self.itinerary_id = itinerary_id or fake.random_int(min=1, max=MAX_CARDS)
        self.charge_id = charge_id or fake.random_int(min=1, max=MAX_CARDS)
