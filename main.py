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
from bus_app.database_functions.model_based.validation_functions import ValidationHelp

connection = sqlite3.connect("./bus.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()


card_functions = CardHelp(cursor, connection)
category_functions = CategoryHelp(cursor, connection)
charge_functions = ChargeHelp(cursor, connection)
validation_functions = ValidationHelp(cursor, connection)


itinerary_functions = ItineraryHelp(cursor, connection)
stop_functions = StopHelp(cursor, connection)
route_functions = RouteHelp(cursor, connection)


console = Console()
app = typer.Typer()


# itinerary
@app.command(short_help="Shows Selected Itinerary's Info")
def get_itinerary_info():
    table = itinerary_table()

    itineraries = itinerary_functions.get_all_itineraries()
    for itinerary in itineraries:
        table.add_row(*[str(c) for c in itinerary])
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


@app.command(short_help="Shows Bus Stop Info as well as the Routes that it Belongs to")
def get_stop_info():
    pass


# personalized_card
@app.command(short_help="Creates Personal Card")
def create_card(name: str, category="normal"):
    from bus_app.entity_models.card import Card
    try:
        card_model = Card(name, category, signup)
        # card_functions.add_card(name, category)
        card_functions.add_card(card_model)
    except sqlite3.IntegrityError:
        typer.echo("Error: Invalid Category")
        return

    last_id = card_functions.cursor.lastrowid
    card_tuple = card_functions.get_card(last_id).pop()

    typer.echo(f"New cardholder {name} with card_id {last_id}")
    table = card_info_table()
    table.add_row(*[str(c) for c in card_tuple])
    console.print(table)


@app.command(short_help="Shows Personal Card Info")
def get_card(card_id: int):
    try:
        card_tuple = card_functions.get_card(card_id).pop()
    except Exception:
        typer.echo("Error: Invalid Card ID")
        return

    typer.echo(f"Card Information")
    table = card_info_table()
    table.add_row(*[str(c) for c in card_tuple])
    console.print(table)


@app.command(short_help="Buy Ticket with Personal Card")
def add_ticket(card_id: int, total_tickets=1):
    TICKET_PRICE = 1.0
    try:
        card_tuple = card_functions.get_card(card_id).pop()
        category_id = card_tuple[2]

        discount = category_functions.get_discount(category_id).pop()[0]
    except Exception:
        typer.echo("Error: Invalid Card ID")
        return
    
    pay = TICKET_PRICE * int(total_tickets) * (1 - discount)
    typer.echo(f"Category {category_id} Discount: {discount}")
    typer.echo(f"Total Pay: {pay}")
    
    charge_functions.add_charge(total_tickets, pay, card_id, category_id)

    card_functions.update_balance(card_id, total_tickets)
    card_tuple = card_functions.get_card(card_id).pop()

    typer.echo(f"Card Information")
    table = card_info_table()
    table.add_row(*[str(c) for c in card_tuple])
    console.print(table)


@app.command(short_help="Validate Ticket with Personal Card")
def embark_ticket(card_id: int, itinerary_id: int):
    try:
        card_tuple = card_functions.get_card(card_id).pop()
        card_balance = card_tuple[3]
    except Exception:
        typer.echo("Error: Invalid Card ID")
        return
    
    if card_balance > 0:
        validation_functions.validate_ticket(card_id, itinerary_id)
    else:
        typer.echo("Error: Insufficient Balance")
        return
    
    card_functions.update_balance(card_id, -1)
    card_tuple = card_functions.get_card(card_id).pop()

    typer.echo(f"Card Information")
    table = card_info_table()
    table.add_row(*[str(c) for c in card_tuple])
    console.print(table)

@app.command(short_help="Disembark Ticket with Personal Card")
def disembark_ticket(card_id: int, itinerary_id: int):
    pass


@app.command(short_help="Show Total Tickets of Bus Route")
def total_tickets(start_date: str, end_date: str):
    pass


if __name__ == "__main__":
    category_functions.add_category(name="normal", discount=0.0)
    category_functions.add_category(name="student", discount=0.5)
    category_functions.add_category(name="elderly", discount=0.25)
    category_functions.add_category(name="unemployed", discount=0.45)
    category_functions.add_category(name="military", discount=0.55)
    category_functions.add_category(name="disability", discount=0.65)

    app()
