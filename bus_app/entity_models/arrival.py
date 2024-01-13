from faker import Faker
from datetime import timedelta

Faker.seed(1234)
fake = Faker(locale="el_GR")

MAX_CARDS = 10


class Arrival:
    def __init__(
        self,
        itinerary_id=None,
        stop_id=None,
        real_toa=None,
    ):
        self.itinerary_id = itinerary_id or fake.unique.random_int(min=1, max=MAX_CARDS)
        self.stop_id = stop_id or fake.random_int(min=1, max=MAX_CARDS)
        self.real_toa = real_toa or fake.date_time_this_decade(
            before_now=False
        )
