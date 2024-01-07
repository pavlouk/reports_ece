import datetime


class route:
    def __init__(self, route_name, 
                  stops: list):
        self.route_name = route_name  
        self.stops = stops ## 2D list: [[ stop_id, stop_position, estTOA],...]
        
    def __repr__(self) -> str:
        return f"Route details:[ route_name: {self.route_name},stops: {self.stops} ]"