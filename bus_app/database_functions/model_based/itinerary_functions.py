from datetime import datetime
from bus_app.entity_models.itinerary import itinerary


class ItHelp:
    def __init__(self, cursor, 
                  connection):
        self.cursor = cursor
        self.connection = connection

    ##itinerary functions
    def insert_itinerary(self, itinerary: itinerary):
        with self.connection:
            self.cursor.execute(f'INSERT INTO \'itinerary\' (\'starting_time\',\'direction\',\'routeName\',\'busId\',\'driverId\') \
            VALUES (\'{itinerary.starting_time}\', \'{itinerary.direction}\', \'{itinerary.route_name}\', \'{itinerary.bus_id}\', \'{itinerary.driver_id}\')')


    def get_all_itineraries(self):
        self.cursor.execute('select * from itinerary')
        results = self.cursor.fetchall()
        itinerarys = []
        for result in results:
            itinerarys.append(result)
        return(itinerarys)


    def delete_itinerary(self, itinerary_id: int):
        with self.connection:    
            self.cursor.execute(f"DELETE from itinerary WHERE id={itinerary_id}")

    def set_itinerary_ending_time(self, itinerary_id: int):
        with self.connection:    
            self.cursor.execute(f"UPDATE itinerary SET \'ending_time\'=\'{str(datetime.now())}\' WHERE \'id\'=\'{itinerary_id}\'")

