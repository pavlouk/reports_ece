from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")


class Driver:
    def __init__(self, hired_date=None, availiability=None, name=None):
        self.hired_date = hired_date or fake.date_between(
            start_date="-30y", end_date="today"
        )
        self.availiability = (
            availiability or fake.random_choices(elements=[True, False], length=1).pop()
        )
        self.name = name or fake.name()
