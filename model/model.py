import networkx as nx
import database.DAO
class Model:
    def __init__(self):
        self.airports = None
        self.flights = None
        self.dictionary = {}

    def buildGraphs(self, distance):
        graph = nx.Graph()

        self.airports = database.DAO.DAO().getAllNodes()
        for a in self.airports:
            graph.add_node(a.id)

        self.flights = database.DAO.DAO().getAllFlights()
        for i in self.flights:
            #print('________')
            if (i.original_airport, i.destination_airport) in self.dictionary:
                self.dictionary[(i.original_airport, i.destination_airport)].append(i.distance)
            elif (i.destination_airport, i.original_airport) in self.dictionary:
                self.dictionary[(i.destination_airport, i.original_airport)].append(i.distance)
            else:
                self.dictionary[(i.original_airport, i.destination_airport)] = [i.distance]
        dizionario = {}
        for d in self.dictionary:
            media = self.calcolamedia(self.dictionary[d])
            if media > int(distance):
                dizionario[d] = media
        return dizionario






    def calcolamedia(self, distanze):
        media = 0
        for i in distanze:
            media+=i
        media = media/len(distanze)
        return media