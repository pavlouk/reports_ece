from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")


class Bus:
    def __init__(self, status=None, capacity=None):
        self.status = (
            status
            or fake.random_choices(
                elements=[
                    "operational",
                    "maintenance",
                ],
                length=1,
            ).pop()
        )
        self.capacity = (
            capacity
            or fake.random_choices(
                elements=[
                    50,
                    100,
                    200,
                ],
                length=1
            ).pop()
        )
