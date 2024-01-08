import datetime


class card:
    def __init__(self, ticket_id, passenger_name, balance=0, category_name=None):
        self.ticket_id = ticket_id
        self.balance = balance
        self.category_name = category_name
        self.passenger_name = passenger_name

    def __repr__(self) -> str:
        return f"Personalized_card details:[ ticket_id: {self.ticket_id},passenger_name: {self.passenger_name}\
            ,passenger_name: {self.passenger_name},balance: {self.balance} ]"
