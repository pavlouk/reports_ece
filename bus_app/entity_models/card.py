class Card:
    def __init__(self, *args):
        self.ticket_id = args[0]
        self.passenger_name = args[1]
        self.category_name = args[2]
        self.balance = args[3]

    def __str__(self):
        return f"{self.ticket_id} {self.passenger_name} {self.category_name} {self.balance}"
