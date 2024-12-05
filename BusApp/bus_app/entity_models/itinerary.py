from faker import Faker
from datetime import timedelta

Faker.seed(1234)
fake = Faker(locale="el_GR")

MAX_CARDS = 10


class Itinerary:
    def __init__(
        self,
        starting_time=None,
        ending_time=None,
        direction=None,
        route_name=None,
        bus_id=None,
        driver_id=None,
    ):
        self.starting_time = starting_time or fake.date_time_this_decade(
            before_now=False
        )
        self.ending_time = ending_time or (
            self.starting_time + timedelta(minutes=fake.random_int(min=10, max=30))
        )
        self.direction = (
            direction or fake.random_choices(elements=[True, False], length=1).pop()
        )
        self.route_name = route_name or f"{fake.city()} - {fake.city()}".upper()
        self.bus_id = bus_id or fake.random_int(min=1, max=MAX_CARDS)
        self.driver_id = driver_id or fake.random_int(min=1, max=MAX_CARDS)
