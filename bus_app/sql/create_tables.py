CREATE_CARD_TABLE = """
CREATE TABLE IF NOT EXISTS "Card" (
	"id"	INTEGER NOT NULL,
	"passenger_name"	varchar(50) NOT NULL,
	"category_name"	varchar(50) NOT NULL,
	"balance"	float NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_CATEGORY_TABLE = """
CREATE TABLE IF NOT EXISTS "Category" (
	"discount"	float NOT NULL,
	"category_name"	varchar(50) NOT NULL,
	PRIMARY KEY("category_name")
);
"""
CREATE_ROUTE_TABLE = """
CREATE TABLE IF NOT EXISTS "Route" (
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("name")
);
"""
CREATE_STOP_TABLE = """
CREATE TABLE IF NOT EXISTS "Stop" (
	"id"	INTEGER NOT NULL,
	"name"	varchar(50) NOT NULL,
	"location"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_DRIVER_TABLE = """
CREATE TABLE IF NOT EXISTS "Driver" (
	"id"	INTEGER NOT NULL,
	"hired_date"	date NOT NULL,
	"availiability"	bool NOT NULL DEFAULT 1,
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_BUS_TABLE = """
CREATE TABLE IF NOT EXISTS "Bus" (
	"id"	INTEGER NOT NULL,
	"status"	varchar(50) NOT NULL DEFAULT 'normal',
	"capacity"	INTEGER DEFAULT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_ARRIVAL_TABLE = """
CREATE TABLE IF NOT EXISTS "Arrives" (
	"itinerary_id"	INTEGER NOT NULL,
	"stop_id"	INTEGER NOT NULL,
	"real_toa"	datetime NOT NULL,
	FOREIGN KEY("itinerary_id") REFERENCES "Itinerary"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("stop_id") REFERENCES "Stop"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
"""
CREATE_CONSISTS_TABLE = """
CREATE TABLE IF NOT EXISTS "Consists" (
	"stop_id"	varchar(50) NOT NULL,
	"route_name"	varchar(50) NOT NULL,
	FOREIGN KEY("stop_id") REFERENCES "Route"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("route_name") REFERENCES "Stop"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("stop_id","route_name")
);
"""
CREATE_ITINERARY_TABLE = """
CREATE TABLE IF NOT EXISTS "Itinerary" (
	"id"	INTEGER NOT NULL,
	"starting_time"	date NOT NULL DEFAULT '',
	"ending_time"	date DEFAULT NULL,
	"direction"	bool NOT NULL DEFAULT 1,
	"routeName"	varchar(50) NOT NULL DEFAULT '',
	"busId"	varchar(50) NOT NULL DEFAULT '',
	"driverId"	varchar(50) NOT NULL DEFAULT '',
	FOREIGN KEY("driverId") REFERENCES "Driver"("id"),
	FOREIGN KEY("routeName") REFERENCES "Route"("name"),
	FOREIGN KEY("busId") REFERENCES "Bus"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
CREATE_VALIDATION_TABLE = """
CREATE TABLE IF NOT EXISTS "Validate" (
	"card_id"	INTEGER NOT NULL,
	"itinerary_id"	INTEGER NOT NULL,
	"embarkation_time"	datetime NOT NULL DEFAULT '',
	"dissembarkation_time"	datetime DEFAULT NULL,
	FOREIGN KEY("itinerary_id") REFERENCES "Itinerary"("id") ON UPDATE CASCADE,
	FOREIGN KEY("card_id") REFERENCES "Card"("id") ON UPDATE CASCADE,
	PRIMARY KEY("card_id","itinerary_id")
);
"""
