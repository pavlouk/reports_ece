import sqlite3
from datetime import datetime
from bus_app.entity_models.card import card


class CardHelp:
    def __init__(self, cursor, 
                  connection):
        self.cursor = cursor
        self.connection = connection

    ##itinerary functions
    def insert_itinerary(self, card: card):
        self.cursor.execute('select count(*) FROM itinerary')
        count = self.cursor.fetchone()[0]
        with self.connection:
            self.cursor.execute('INSERT INTO itinerary VALUES (:scheduleId, :direction, :starting_time, :ending_time)',
            {'scheduleId': card.scheduleId, 'direction': card.direction, 'starting_time': card.starting_time,
            'ending_time': card.ending_time})


    def get_all_itineraries(self):
        self.cursor.execute('select * from itinerary')
        results = self.cursor.fetchall()
        itinerarys = []
        for result in results:
            itinerarys.append(result)
        return(itinerarys)


    def delete_itinerary(self, itinerary_id: int):
        with self.connection:    
            self.cursor.execute("DELETE from itinerary WHERE itinerary_id={itinerary_id}")
