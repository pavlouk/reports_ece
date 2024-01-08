from datetime import datetime
from bus_app.entity_models.route import Route
from bus_app.sql.create_tables import CREATE_ROUTE_TABLE

class RouteHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_ROUTE_TABLE)
        
    def add_route(self, name: str, route_stops: list[str]):
        pass