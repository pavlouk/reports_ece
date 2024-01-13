from datetime import datetime
import typer
import sqlite3
from rich.console import Console

from bus_app.rich import itinerary_table, card_info_table

from bus_app import (
    card_functions,
    category_functions,
    purchase_functions,
    validation_functions,
    arrival_functions,
    consists_functions,
    itinerary_functions,
    stop_functions,
    route_functions,
    bus_functions,
    driver_functions,
    disembark_functions,
    charge_functions,
)
from bus_app.entity_models import (
    Bus,
    Card,
    Driver,
    Itinerary,
    Purchase,
    Route,
    Stop,
    Consists,
    Validation,
    Arrival,
    Disembark,
    Charge,
)

console = Console()
app = typer.Typer()


# itinerary
@app.command(short_help="Shows Selected Itinerary's Info")
def get_itinerary_info():
    table = itinerary_table()

    itineraries = itinerary_functions.get_itineraries()
    for itinerary in itineraries:
        table.add_row(*[str(c) for c in itinerary])
    console.print(table)


@app.command(short_help="Shows Bus Stop Info")
def get_stop_info():
    stop_tuple = stop_functions.get_stop(stop_id).pop()

    typer.echo(f"Stop Information")
    table = stop_info_table()
    table.add_row(*[str(c) for c in stop_tuple])
    console.print(table)


# personalized_card
@app.command(short_help="Creates Personal Card")
def create_card(name: str, category="normal"):
    try:
        card_functions.add_card(
            Card(
                passenger_name=name,
                category=category,
                signup_date=str(datetime.now().date()),
            )
        )
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


@app.command(short_help="Purchase balance to Personal Card")
def purchase_balance(card_id: int, amount=1.0):
    try:
        card_tuple = card_functions.get_card(card_id).pop()
    except Exception:
        typer.echo("Error: Invalid Card ID")
        return

    typer.echo(f"Purchased Amount: {amount}")

    purchase_functions.add_purchase(
        Purchase(
            card_id=card_id,
            purchased_balance=amount,
            purchase_date=str(datetime.now().date()),
        )
    )
    card_tuple = card_functions.get_card(card_id).pop()

    typer.echo(f"Card Information")
    table = card_info_table()
    table.add_row(*[str(c) for c in card_tuple])
    console.print(table)


@app.command(short_help="Embark Bus with Personal Card")
def embark_ticket(card_id: int, itinerary_id: int):
    try:
        card_tuple = card_functions.get_card(card_id).pop()
        card_balance = card_tuple[3]
    except Exception:
        typer.echo("Error: Invalid Card ID")
        return

    if card_balance > 0:
        validation_functions.add_validation(card_id, itinerary_id)
    else:
        typer.echo("Error: Insufficient Balance")
        return

    # card_functions.update_balance(card_id, -1)
    card_tuple = card_functions.get_card(card_id).pop()

    typer.echo(f"Card Information")
    table = card_info_table()
    table.add_row(*[str(c) for c in card_tuple])
    console.print(table)


@app.command(short_help="Disembark Bus with Personal Card")
def disembark_ticket(card_id: int, itinerary_id: int):
    TICKET_PRICE = 1.0
    try:
        card_tuple = card_functions.get_card(card_id).pop()
        category_id = card_tuple[2]

        discount = category_functions.get_discount(category_id).pop()[0]
    except Exception:
        typer.echo("Error: Invalid Card ID")
        return

    pay = TICKET_PRICE * (1 - discount)
    typer.echo(f"Category {category_id} Discount: {discount}")
    typer.echo(f"Total Pay: {pay}")

    # charge_functions.add_charge(purchased_balance, pay, card_id, category_id)
    # card_functions.update_balance(card_id, purchased_balance)
    card_tuple = card_functions.get_card(card_id).pop()

    typer.echo(f"Card Information")
    table = card_info_table()
    table.add_row(*[str(c) for c in card_tuple])
    console.print(table)


@app.command(short_help="Show Total income of the company")
def company_balance(start_date=None, end_date=None):
    if not start_date and not end_date:
        typer.echo(purchase_functions.get_all_earnings().pop()[0])
        return
    
    typer.echo(purchase_functions.get_earnings(start_date, end_date).pop()[0])
    

if __name__ == "__main__":
    if not category_functions.get_categories():
        from faker import Faker

        fake1 = Faker("el_GR")
        fake1.seed_instance(0)

        fake2 = Faker("el_GR")
        fake2.seed_instance(0)

        fake3 = Faker("el_GR")
        fake3.seed_instance(0)

        MAX_CARDS = 100

        category_functions.add_category(name="normal", discount=0.0)
        category_functions.add_category(name="student", discount=0.5)
        category_functions.add_category(name="student", discount=0.25)
        category_functions.add_category(name="unemployed", discount=0.45)
        category_functions.add_category(name="military", discount=0.55)
        category_functions.add_category(name="disability", discount=0.65)

        for _ in range(10):
            route_functions.add_route(
                Route(name=f"{fake1.city()} - {fake1.city()}".upper())
            )

        for _ in range(10):
            stop_functions.add_stop(Stop())

        for _ in range(10):
            bus_functions.add_bus(Bus())
            driver_functions.add_driver(Driver())

        for i in range(10):
            name = f"{fake2.city()} - {fake2.city()}".upper()
            for i in range(1, 11):
                consists_functions.add_consists(Consists(route_name=name, stop_id=i))

        for _ in range(10):
            itinerary_functions.add_itinerary(
                Itinerary(route_name=f"{fake3.city()} - {fake3.city()}".upper())
            )

        for _ in range(MAX_CARDS):
            card_functions.add_card(Card())

        for _ in range(MAX_CARDS):
            purchase_functions.add_purchase(Purchase())

        for _ in range(MAX_CARDS):
            validation_functions.add_validation(Validation())

        for _ in range(10):
            arrival_functions.add_arrival(Arrival())

        for _ in range(10):
            charge_functions.add_charge(Charge())

        for _ in range(10):
            disembark_functions.add_disembark(Disembark())

    app()
