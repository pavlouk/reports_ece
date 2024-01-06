import typer
from rich.console import Console
from bus_app.dataclasses import Todo
from bus_app.rich import get_todos_table, COLORS
from bus_app.database import (
    create_table,
)

console = Console()

app = typer.Typer()

todos_table = get_todos_table()


@app.command(short_help="Shows Personal Card Info")
def get_card_info():
    pass

@app.command(short_help="Creates Personal Card")
def create_card():
    pass

@app.command(short_help="Buy Ticket with Personal Card")
def buy_card_ticket():
    # Usage:
    # python -m BusApp.main buy-card-ticket 123 <- ticket_id
    # --category student 
    # --total-tickets 1 
    # --price-id 2
    pass

@app.command(short_help="Validate Ticket with Personal Card")
def validate_card_ticket():
    pass

@app.command(short_help="Shows next Bus Arrivals")
def get_bus_stop_info():
    pass

@app.command(short_help="Show Total Tickets of Bus Route")
def show_total_tickets(start_date: str, end_date: str):
    pass

if __name__ == "__main__":
    create_table()
    app()
