INSERT_CARD = "INSERT INTO Card (passenger_name, category_name) VALUES (?, ?)"
INSERT_CATEGORY = "INSERT INTO Category (discount, category_name) VALUES (?, ?)"
INSERT_CHARGE = "INSERT INTO Charge (discount, category_name) VALUES (?, ?)"

INSERT_ARRIVAL = "INSERT INTO Arrives (name) VALUES (?)"
INSERT_STOP = "INSERT INTO Stop (name, location) VALUES (?, ?)"
INSERT_ROUTE = "INSERT INTO Route (name) VALUES (?)"

INSERT_ITINERARY = "INSERT INTO Itinerary (starting_time, direction, routeName, busId, driverId) VALUES (?,?,?,?,?)"
INSERT_BUS = "INSERT INTO Bus (name) VALUES (?)"
INSERT_DRIVER = "INSERT INTO Driver (name) VALUES (?)"
INSERT_CONSIST = "INSERT INTO Consists (name) VALUES (?)"
