
class Itinerary:
    def __init__(
        self,
        starting_time=None,
        direction=None,
        bus_id=None,
        route_name=None,
        driver_id=None,
        ending_time=None,
    ):
        self.starting_time = starting_time
        self.direction = direction
        self.bus_id = bus_id
        self.route_name = route_name
        self.driver_id = driver_id
        self.ending_time = ending_time
