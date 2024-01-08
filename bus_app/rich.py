from rich.table import Table

def itinerary_table():
    table = Table(show_header=True, header_style="bold blue")
    
    table.add_column("id", style="dim", width=2)
    table.add_column("Starting Time", min_width=8)
    table.add_column("Ending Time", min_width=4, justify="right")
    table.add_column("Direction", min_width=4, justify="right")
    table.add_column("Route Name", min_width=4, justify="right")
    table.add_column("Bus id", min_width=4, justify="right")
    table.add_column("Driver id", min_width=4, justify="right")
    
    return table

def card_info_table():
    table = Table(show_header=True, header_style="bold blue")
    
    table.add_column("id", style="dim", width=2)
    table.add_column("Card Number", min_width=8)
    table.add_column("Balance", min_width=4, justify="right")
    
    return table
