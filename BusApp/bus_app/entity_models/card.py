from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")

class Card:
    def __init__(self, passenger_name=None, category_name=None, signup_date=None):
        self.passenger_name = passenger_name or fake.name()
        self.category_name = (
            category_name
            or fake.random_choices(
                elements=[
                    "normal",
                    "student",
                    "student",
                    "unemployed",
                    "military",
                    "disability",
                ],
                length=1,
            ).pop()
        )
        self.signup_date = signup_date or fake.date()
