from database.DB_connect import DBConnect
from model.airports import Airport
from model.flights import Flight


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """ SELECT ID 
             FROM airports
        """

        cursor.execute(query)

        for row in cursor:
            result.append(
                Airport(row['ID']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllFlights():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * 
                 FROM flights
            """

        cursor.execute(query)

        for row in cursor:
            result.append(
                Flight(row['ID'],
                       row['ORIGIN_AIRPORT_ID'],
                       row['DESTINATION_AIRPORT_ID'],
                       row['DISTANCE']))

        cursor.close()
        conn.close()
        return result