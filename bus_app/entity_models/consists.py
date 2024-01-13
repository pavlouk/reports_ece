from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")

MAX_STOPS = 10


class Consists:
    def __init__(
        self, stop_id=None, route_name=None, stop_position=None, est_next_stop_toa=None
    ):
        self.stop_id = stop_id or fake.random_int(min=1, max=MAX_STOPS)
        self.route_name = route_name or f"{fake.city()} - {fake.city()}".upper()
        self.stop_position = stop_position or fake.random_int(max=MAX_STOPS)
        self.est_next_stop_toa = est_next_stop_toa or float(
            fake.random_int(max=MAX_STOPS) / 2.0
        )
