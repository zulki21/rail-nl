from loader import load_stations
import random
from connection import Train

def get_k(trains, used_connections, minutes):

    return 10000 * (used_connections / 28) - (trains * 100 + minutes)

class GreedyAlgo:
    def __init__(self):
        self.stations = load_stations()
        self.trains = []
        self.used_connections = []

        while len(self.used_connections) != 28:

            # create starting station
            current_train = Train(random.choice(list(self.stations.values())))
            self.trains.append(current_train)
            
            while current_train.get_time_route() < 120:

                current_station = current_train.get_route()[-1]

                connections = current_station.connections

                for connection in connections:
                    



            # Chose which track is best for train (k value)

            # Let run for 120 min

            # repeat untill all tracks used


a = GreedyAlgo()

