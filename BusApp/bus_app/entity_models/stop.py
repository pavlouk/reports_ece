from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")

class Stop:
    def __init__(self, name=None, location=None):
        self.name = name or fake.street_name()
        self.location = location or fake.street_address()

