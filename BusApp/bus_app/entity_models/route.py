from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")

class Route:
    def __init__(self, name=None):
        self.name = name or f"{fake.city()} - {fake.city()}".upper()