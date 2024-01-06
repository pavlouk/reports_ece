from rich.table import Table

COLORS = {
    "Learn": "cyan",
    "YouTube": "red",
    "Sports": "cyan",
    "Study": "green",
}

def get_todos_table():
    table = Table(show_header=True, header_style="bold blue")
    
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")
    
    return table
