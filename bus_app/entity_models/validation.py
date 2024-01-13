from faker import Faker
from datetime import timedelta

Faker.seed(1234)
fake = Faker(locale="el_GR")

MAX_CARDS = 10


class Validation:
    def __init__(
        self,
        card_id=None,
        itinerary_id=None,
        embarkation_time=None,
    ):
        self.card_id = card_id or fake.random_int(min=1, max=MAX_CARDS)
        self.itinerary_id = itinerary_id or fake.random_int(min=1, max=MAX_CARDS)
        self.embarkation_time = embarkation_time or fake.date_time_this_decade(
            before_now=False
        )
