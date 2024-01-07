import datetime


class itinerary:
    def __init__(
        self,
        starting_time: str,
        direction,
        bus_id,
        route_name,
        driver_id,
        ending_time=None,
    ):
        self.bus_id = bus_id
        self.driver_id = driver_id
        self.route_name = route_name
        self.direction = direction
        self.starting_time = starting_time
        self.ending_time = ending_time if ending_time is not None else None

    def __repr__(self) -> str:
        return f"Itinerary details:[ driver_id: {self.driver_id},route_name: {self.route_name},id: {self.id},direction: {self.direction},starting_time: {self.starting_time},ending_time: {self.ending_time} ]"
