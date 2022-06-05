from dataclasses import dataclass
from typing import Any, Protocol

@dataclass
class Movement:
    direction: str
    distance: int
    obj: Any

class RunnerProtocol(Protocol):
    def run(self, direction):
        """This is Runner Protocol"""

class FlyerProtocol(Protocol):
    def fly(self, direction):
        """This is Flyer Protocol"""


class Runner:
    def run(self, directions):
        if directions[0] != directions[1]:
            return Movement(obj=self, direction=directions, distance=0)
        return Movement(obj=self, direction=directions, distance=10)

class Flyer:
    def fly(self, directions):
        if directions[0] != directions[1]:
            return Movement(obj=self, direction=directions, distance=0)

        return Movement(obj=self, direction=directions, distance=10000)


class Controller:
    def make_flight(self, obj: FlyerProtocol, direction):
        return obj.fly(direction)
    
    def make_run(self, obj: RunnerProtocol, direction):
        return obj.run(direction)


def main() -> None:
    c = Controller()
    flight_move = c.make_flight(Flyer(), ['south', 'south'])
    run_move = c.make_run(Runner(), 'north')
    print(flight_move.distance, flight_move.direction)

if __name__ == '__main__':
    main()
