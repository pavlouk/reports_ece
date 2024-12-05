import sqlite3

from .database_functions import DisembarkHelp
from .database_functions import CardHelp
from .database_functions import CategoryHelp
from .database_functions import BusHelp
from .database_functions import DriverHelp
from .database_functions import ItineraryHelp
from .database_functions import PurchaseHelp
from .database_functions import StopHelp
from .database_functions import RouteHelp
from .database_functions import ValidationHelp
from .database_functions import ConsistsHelp
from .database_functions import ArrivalHelp
from .database_functions import ChargeHelp

connection = sqlite3.connect("./bus.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

card_functions = CardHelp(cursor, connection)
category_functions = CategoryHelp(cursor, connection)
purchase_functions = PurchaseHelp(cursor, connection)
validation_functions = ValidationHelp(cursor, connection)
arrival_functions = ArrivalHelp(cursor, connection)
consists_functions = ConsistsHelp(cursor, connection)
itinerary_functions = ItineraryHelp(cursor, connection)
stop_functions = StopHelp(cursor, connection)
route_functions = RouteHelp(cursor, connection)
bus_functions = BusHelp(cursor, connection)
driver_functions = DriverHelp(cursor, connection)
disembark_functions = DisembarkHelp(cursor, connection)
charge_functions = ChargeHelp(cursor, connection)