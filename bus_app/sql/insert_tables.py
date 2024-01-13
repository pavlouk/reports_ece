INSERT_CHARGE = "INSERT INTO Charge (purchase_date, tickets, pay, card_id, category_id) VALUES (?, ?, ?, ?, ?)"
INSERT_PURCHASE = "INSERT INTO Purchase (purchase_date, purchased_balance, card_id) VALUES (?, ?, ?)"
INSERT_CARD = "INSERT INTO Card (passenger_name, category_name, signup_date) VALUES (?, ?, ?)"
INSERT_CATEGORY = "INSERT OR IGNORE INTO Category (name, discount) VALUES (?, ?)"
INSERT_VALIDATION = "INSERT OR IGNORE INTO Validation (card_id, itinerary_id, embarkation_time, disembarkation_time) VALUES (?, ?)"

INSERT_CONSISTS = "INSERT INTO Consists (stop_id, route_name, stop_position, est_next_stop_toa) VALUES (?, ?, ?, ?)"
INSERT_STOP = "INSERT OR IGNORE INTO Stop (name, location) VALUES (?, ?)"
INSERT_ROUTE = "INSERT OR IGNORE INTO Route (name) VALUES (?)"
INSERT_ARRIVAL = "INSERT INTO Arrives (name) VALUES (?)"

INSERT_ITINERARY = "INSERT INTO Itinerary (starting_time, direction, route_name, bus_id, driver_id) VALUES (?,?,?,?,?)"
INSERT_BUS = "INSERT OR IGNORE INTO Bus (status, capacity) VALUES (?, ?)"
INSERT_DRIVER = "INSERT OR IGNORE INTO Driver (hired_date, availiability, name) VALUES (?, ?, ?)"
