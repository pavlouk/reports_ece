import typer
import sqlite3
from rich.console import Console
from bus_app.entity_models.itinerary import itinerary
from bus_app.database_functions.model_based.itinerary_functions import ItHelp
from bus_app.database_functions.model_based.card_functions import CardHelp
from bus_app.sql.create_tables import (
    CREATE_CARD_TABLE,
    CREATE_CATEGORY_TABLE,
    CREATE_STOP_TABLE,
    CREATE_ROUTE_TABLE,
    CREATE_BUS_TABLE,
    CREATE_DRIVER_TABLE,
    CREATE_ARRIVAL_TABLE,
    CREATE_CONSISTS_TABLE,
    CREATE_ITINERARY_TABLE
)

connection = sqlite3.connect("./bus.db")
cursor = connection.cursor()


itinerary_functions = ItHelp(cursor, connection)
card_functions = CardHelp(cursor, connection)

console = Console()
app = typer.Typer()


##itinerary
@app.command(short_help="Shows Selected Itinerary's Info")
def get_itinerary_info():
    print(itinerary_functions.get_all_itineraries())
    pass


@app.command(short_help="Creates Personal Card")
def insert_itinerary():
    itinerary_functions.insert_itinerary(itinerary("2019-01-14", 1, 1, 1, 1, None))
    pass


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
@app.command(short_help="Shows Personal Card Info")
def get_card_info():
    pass


@app.command(short_help="Creates Personal Card")
def create_card():
    pass


@app.command(short_help="Buy Ticket with Personal Card")
def buy_card_ticket():
    # python main.py buy-card-ticket 
    # --card-id 123
    # --category student
    # --total-tickets 1
    # --price-id 2
    pass


@app.command(short_help="Validate Ticket with Personal Card")
def validate_card_ticket():
    pass


@app.command(short_help="Shows Bus Stop Info as well as the Routes that it Belongs to")
def get_bus_stop_info():
    pass


@app.command(short_help="Show Total Tickets of Bus Route")
def show_total_tickets(start_date: str, end_date: str):
    pass


if __name__ == "__main__":
    cursor.executescript(CREATE_CARD_TABLE)
    cursor.executescript(CREATE_CATEGORY_TABLE)
    cursor.executescript(CREATE_STOP_TABLE)
    cursor.executescript(CREATE_ROUTE_TABLE)
    cursor.executescript(CREATE_BUS_TABLE)
    cursor.executescript(CREATE_DRIVER_TABLE)
    cursor.executescript(CREATE_ARRIVAL_TABLE)
    cursor.executescript(CREATE_CONSISTS_TABLE)
    cursor.executescript(CREATE_ITINERARY_TABLE)
    app()
