from bus_app.entity_models.route import Route
from bus_app.sql.create_tables import CREATE_ROUTE_TABLE
from bus_app.sql.insert_tables import INSERT_ROUTE

class RouteHelp:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_ROUTE_TABLE)
        
    def add_route(self, route: Route):
        with self.connection:
            self.cursor.execute(INSERT_ROUTE, (route.name,))