SELECT_CARD_INFO = "SELECT id, passenger_name, category_name, balance FROM Card WHERE id = (?)"
SELECT_CATEGORY_DISCOUNT = "SELECT discount FROM Category WHERE name = ?"
SELECT_CATEGORIES = "SELECT * FROM Category"

SELECT_CHARGES_BY_DATE = "SELECT * FROM Charge WHERE date_time BETWEEN ? AND ?"