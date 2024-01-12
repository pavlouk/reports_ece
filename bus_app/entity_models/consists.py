from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")

MAX_STOPS = 10

class Consists:
    def __init__(self, stop_id=None, route_name=None, stop_position=None, est_next_stop_toa=None):
        self.stop_id = stop_id or fake.street_name()
        self.route_name = route_name or f"{fake.city()} - {fake.city()}".upper()
        self.stop_position = stop_position or fake.street_address()
        self.est_next_stop_toa = est_next_stop_toa or fake.street_address()

