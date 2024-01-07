import datetime


class card:
    def __init__(self, ticket_id, 
                  passenger_name,balance=0,cadegory_name=None):
        self.ticket_id = ticket_id  
        self.balance = balance 
        self.cadegory_name = cadegory_name if cadegory_name is not None else None
        self.passenger_name = passenger_name 
        
    def __repr__(self) -> str:
        return f"Personalized_card details:[ ticket_id: {self.ticket_id},passenger_name: {self.passenger_name}\
            ,passenger_name: {self.passenger_name},balance: {self.balance} ]"


