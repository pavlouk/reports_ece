from dataclasses import dataclass
from typing import Any, Protocol, List

@dataclass
class Movement:
    directions: List[str]
    distance: int
    obj: Any

# abstact protocol class
class RunnerProtocol(Protocol):
    def run(self, direction):
        """This is the class Runner Protocol"""

# abstact protocol class
class FlyerProtocol(Protocol):
    def fly(self, direction):
        """This is the class Flyer Protocol"""

# concrete class
# concrete method contains behavior and returns according data
class Runner:
    def run(self, directions: List) -> Movement:
        print("hey flyer i known what directions", directions)
        if directions[0] != directions[1]:
            return Movement(obj=self, directions=directions, distance=0)
        return Movement(obj=self, direction=directions, distance=10)

# concrete class
# concrete method contains behavior and returns according data 
class Flyer:
    def fly(self, directions: List) -> Movement:
        print("hey flyer i known what directions", directions)
        if directions[0] != directions[1]:
            return Movement(obj=self, directions=directions, distance=0)
        return Movement(obj=self, direction=directions, distance=10000)


class Controller:
    def make_flight(self, obj: FlyerProtocol, directions:List) -> Movement:
        return obj.fly(directions)
    
    def make_run(self, obj: RunnerProtocol, directions:List) -> Movement:
        return obj.run(directions)


def main() -> None:
    c = Controller()
    # passing concrete dependency
    flight_move = c.make_flight(Flyer(), ['south', 'south'])
    run_move = c.make_run(Runner(), 'north')
    print(flight_move.distance, flight_move.direction, run_move.distance, run_move.direction)

if __name__ == '__main__':
    main()
