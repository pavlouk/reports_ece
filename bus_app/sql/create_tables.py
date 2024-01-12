CREATE_CARD_TABLE = """
CREATE TABLE IF NOT EXISTS Card (
	id	INTEGER NOT NULL,
	passenger_name	varchar(50) NOT NULL,
	category_name	varchar(50) NOT NULL REFERENCES Category(name),
 	signup_date	datetime NOT NULL DEFAULT '',
	balance	float NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_CATEGORY_TABLE = """
CREATE TABLE IF NOT EXISTS Category (
	"name"	varchar(50) NOT NULL,
	"discount"	float NOT NULL,
	PRIMARY KEY("name")
);
"""
CREATE_CHARGE_TABLE = """
CREATE TABLE IF NOT EXISTS "Charge" (
	"id"	INTEGER,
	"disembark_time"	datetime NOT NULL DEFAULT '',
	"amount_charged"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_PURCHASE_TABLE = """
CREATE TABLE IF NOT EXISTS Purchase (
	id INTEGER NOT NULL,
	purchase_date datetime,
	purchased_balance float NOT NULL DEFAULT 0, 
	card_id INTEGER NOT NULL REFERENCES Card(id),	
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_ROUTE_TABLE = """
CREATE TABLE IF NOT EXISTS Route (
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("name")
);
"""
CREATE_STOP_TABLE = """
CREATE TABLE IF NOT EXISTS Stop (
	id	INTEGER NOT NULL,
	name	varchar(50) NOT NULL,
	location	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_DRIVER_TABLE = """
CREATE TABLE IF NOT EXISTS Driver (
	id	INTEGER NOT NULL,
	hired_date	date NOT NULL,
	availiability	bool NOT NULL DEFAULT 1,
	name	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_BUS_TABLE = """
CREATE TABLE IF NOT EXISTS Bus (
	id	INTEGER NOT NULL,
	status	varchar(50) NOT NULL DEFAULT 'operational',
	capacity	INTEGER DEFAULT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_ARRIVAL_TABLE = """
CREATE TABLE IF NOT EXISTS "Arrives" (
	"itinerary_id"	INTEGER NOT NULL,
	"stop_id"	INTEGER NOT NULL,
	"real_toa"	datetime NOT NULL,
 	PRIMARY KEY("stop_id", "itinerary_id"),
	FOREIGN KEY("itinerary_id") REFERENCES "Itinerary"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("stop_id") REFERENCES "Stop"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
"""
CREATE_CONSISTS_TABLE = """
CREATE TABLE IF NOT EXISTS "Consists" (
	"stop_id"	varchar(50) NOT NULL,
	"route_name"	varchar(50) NOT NULL,
 	"stop_position"	INTEGER NOT NULL,
	"est_next_stop_toa"	float NOT NULL DEFAULT 0,
	FOREIGN KEY("stop_id") REFERENCES "Route"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("route_name") REFERENCES "Stop"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("stop_id", "route_name")
);
"""
CREATE_ITINERARY_TABLE = """
CREATE TABLE IF NOT EXISTS "Itinerary" (
	"id"	INTEGER NOT NULL,
	"starting_time"	date NOT NULL DEFAULT '',
	"ending_time"	date DEFAULT NULL,
	"direction"	bool NOT NULL DEFAULT 1,
	"route_name"	varchar(50) NOT NULL DEFAULT '',
	"bus_id"	varchar(50) NOT NULL DEFAULT '',
	"driver_id"	varchar(50) NOT NULL DEFAULT '',
	FOREIGN KEY("driver_id") REFERENCES "Driver"("id"),
	FOREIGN KEY("route_name") REFERENCES "Route"("name"),
	FOREIGN KEY("bus_id") REFERENCES "Bus"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_VALIDATION_TABLE = """
CREATE TABLE IF NOT EXISTS Validation (
	"card_id"	INTEGER NOT NULL,
	"itinerary_id"	INTEGER NOT NULL,
	"embarkation_time"	datetime NOT NULL DEFAULT '',
	FOREIGN KEY("itinerary_id") REFERENCES "Itinerary"("id") ON UPDATE CASCADE,
	FOREIGN KEY("card_id") REFERENCES "Card"("id") ON UPDATE CASCADE,
	PRIMARY KEY("card_id", "itinerary_id")
);
"""
CREATE_DISEMBARKATION_TABLE = """
CREATE TABLE IF NOT EXISTS "Disembarkation" (
	"card_id"	INTEGER NOT NULL,
	"itinerary_id"	INTEGER NOT NULL,
	"charge_id"	INTEGER NOT NULL,
	PRIMARY KEY("card_id", "itinerary_id", "charge_id"),
	FOREIGN KEY("itinerary_id") REFERENCES "itinerary"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("charge_id") REFERENCES "charge"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("card_id") REFERENCES "card"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
"""
CREATE_CARD_BALANCE_CHARGE_TRIGGER_ON_DISEMBARKATION = """
CREATE TRIGGER card_balance_charge
AFTER INSERT ON Disembarkation 
BEGIN
	UPDATE Card SET balance = balance - (
        SELECT Charge.charged_amount
        FROM Charge
        WHERE Charge.id = NEW.charge_id
    )
    WHERE Card.id = NEW.card_id;
END;
"""
CREATE_CARD_BALANCE_FILLUP_ON_PURCHASE_TRIGGER = """
CREATE TRIGGER card_balance_fillup
AFTER INSERT ON Purchase
BEGIN
    UPDATE Card SET balance = balance + NEW.purchased_balance
    WHERE id = NEW.card_id;
END;
"""