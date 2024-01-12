INSERT_CHARGE = "INSERT INTO Charge (purchase_date, tickets, pay, card_id, category_id) VALUES (?, ?, ?, ?, ?)"
INSERT_CARD = "INSERT INTO Card (passenger_name, category_name, signup_date) VALUES (?, ?, ?)"
INSERT_CATEGORY = "INSERT OR IGNORE INTO Category (name, discount) VALUES (?, ?)"
INSERT_VALIDATION = "INSERT OR IGNORE INTO Validation (card_id, itinerary_id, embarkation_time, disembarkation_time) VALUES (?, ?)"

INSERT_CONSIST = "INSERT INTO Consists (name) VALUES (?)"
INSERT_STOP = "INSERT OR IGNORE INTO Stop (name, location) VALUES (?, ?)"
INSERT_ROUTE = "INSERT OR IGNORE INTO Route (name) VALUES (?)"
INSERT_ARRIVAL = "INSERT INTO Arrives (name) VALUES (?)"

INSERT_ITINERARY = "INSERT INTO Itinerary (starting_time, direction, routeName, busId, driverId) VALUES (?,?,?,?,?)"
INSERT_BUS = "INSERT OR IGNORE INTO Bus (status, capacity) VALUES (?, ?)"
INSERT_DRIVER = "INSERT OR IGNORE INTO Driver (hired_date, availiability, name) VALUES (?, ?, ?)"
