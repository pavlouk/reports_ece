INSERT_CHARGE = "INSERT INTO Charge (category_name) VALUES (?, ?)"
INSERT_CARD = "INSERT INTO Card (passenger_name, category_name) VALUES (?, ?)"
INSERT_CATEGORY = "INSERT OR IGNORE INTO Category (category_name, discount) VALUES (?, ?)"

INSERT_CONSIST = "INSERT INTO Consists (name) VALUES (?)"
INSERT_STOP = "INSERT OR IGNORE INTO Stop (name, location) VALUES (?, ?)"
INSERT_ROUTE = "INSERT OR IGNORE INTO Route (name) VALUES (?)"
INSERT_ARRIVAL = "INSERT INTO Arrives (name) VALUES (?)"

INSERT_ITINERARY = "INSERT INTO Itinerary (starting_time, direction, routeName, busId, driverId) VALUES (?,?,?,?,?)"
INSERT_BUS = "INSERT OR IGNORE INTO Bus (name) VALUES (?)"
INSERT_DRIVER = "INSERT OR IGNORE INTO Driver (name) VALUES (?)"
