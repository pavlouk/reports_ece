import typer
import sqlite3
from rich.console import Console
from bus_app.rich import itinerary_table, card_info_table
from bus_app.entity_models.itinerary import Itinerary
from bus_app.database_functions.model_based.itinerary_functions import ItineraryHelp
from bus_app.database_functions.model_based.card_functions import CardHelp
from bus_app.database_functions.model_based.category_functions import CategoryHelp
from bus_app.database_functions.model_based.charge_functions import ChargeHelp
from bus_app.database_functions.model_based.stop_functions import StopHelp
from bus_app.database_functions.model_based.route_functions import RouteHelp

connection = sqlite3.connect("./bus.db")
cursor = connection.cursor()


card_functions = CardHelp(cursor, connection)
category_functions = CategoryHelp(cursor, connection)
charge_functions = ChargeHelp(cursor, connection)

itinerary_functions = ItineraryHelp(cursor, connection)

stop_functions = StopHelp(cursor, connection)
route_functions = RouteHelp(cursor, connection)


console = Console()
app = typer.Typer()


##itinerary
@app.command(short_help="Shows Selected Itinerary's Info")
def get_itinerary_info():
    itinerary_index = 0
    date_index = 1
    bus_index = 2
    route_index = 3
    driver_index = 4
    arrival_index = 5
    card_index = 6

    table = itinerary_table()
    itineraries = itinerary_functions.get_all_itineraries()
    for itinerary in itineraries:
        table.add_row(
            str(itinerary[itinerary_index]),
            itinerary[date_index],
            str(itinerary[bus_index]),
            str(itinerary[route_index]),
            str(itinerary[driver_index]),
            str(itinerary[arrival_index]),
            str(itinerary[card_index]),
        )
    console.print(table)


@app.command(short_help="Creates Personal Card")
def insert_itinerary():
    itinerary_functions.insert_itinerary(Itinerary("2019-01-14", 1, 1, 1, 1, None))


@app.command(short_help="Delete Itinerary")
def delete_itinerary(itinerary_id: int):
    itinerary_functions.delete_itinerary(itinerary_id)
    pass


@app.command(short_help="Completes Itinerary with Ending Time: Now")
def complete_itinerary(itinerary_id: int):
    itinerary_functions.set_itinerary_ending_time(itinerary_id)
    pass


##
##


##personalized_card
@app.command(short_help="Creates Personal Card")
def create_card(name: str, category="student"):
    card_functions.add_card(name, category)
    last_id = card_functions.cursor.lastrowid
    typer.echo(f"Card holder {name} created with card_id {last_id}")
    
    table = card_info_table()

    card_tuple = card_functions.get_card(last_id).pop()
  
    table.add_row(*[str(c) for c in card_tuple])
    console.print(table)


@app.command(short_help="Shows Personal Card Info")
def get_card_info(card_id: int):
    from bus_app.entity_models.card import Card
    # card_dataclass = Card(*card_tuple)
    table = card_info_table()

    card_tuple = card_functions.get_card(card_id).pop()
  
    table.add_row(*[str(c) for c in card_tuple])
    console.print(table)


@app.command(short_help="Buy Ticket with Personal Card")
def buy_card_ticket(card_id: int, category: str, total_tickets: int, price_id: int):
    # python main.py buy-card-ticket
    # --card-id 123
    # --category student
    # --total-tickets 1
    # --price-id 2
    pass


@app.command(short_help="Validate Ticket with Personal Card")
def validate_card_ticket(card_id: int, itinerary_id: int):
    pass


@app.command(short_help="Shows Bus Stop Info as well as the Routes that it Belongs to")
def get_bus_stop_info():
    pass


@app.command(short_help="Show Total Tickets of Bus Route")
def show_total_tickets(start_date: str, end_date: str):
    pass


if __name__ == "__main__":
    category_functions.add_category(name="normal", discount=0.0)
    category_functions.add_category(name="student", discount=0.5)
    category_functions.add_category(name="elderly", discount=0.25)
    category_functions.add_category(name="unemployed", discount=0.45)
    category_functions.add_category(name="military", discount=0.55)
    category_functions.add_category(name="disability", discount=0.65)

    app()
