from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")

MAX_STOPS = 10


class Charge:
    def __init__(
        self, disembark_time=None, amount_charged=None
    ):
        self.disembark_time = disembark_time or fake.date_time_this_decade(
            before_now=False
        )
        self.amount_charged = amount_charged or float(
            fake.random_int(max=MAX_STOPS) / 2.0
        )