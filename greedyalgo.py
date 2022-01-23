from loader import load_stations
import random
from connection import Train

def get_k(trains, used_connections, minutes):

    return 10000 * (used_connections / 28) - (trains * 100 + minutes)

def total_time_trains(trains):
    min = 0
    for train in trains:
        min += train.get_time_route()

    return min

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

                best_k = 0
                for connection in connections:

                    if {current_station, connection} not in self.used_connections:
                       k = get_k(len(self.trains), (len(self.used_connections) + 1), total_time_trains(self.trains) + connection.get_time(current_station))
                    else:
                        k = get_k(len(self.trains), (len(self.used_connections)), total_time_trains(self.trains) + connection.get_time(current_station))
                    







            # Chose which track is best for train (k value)

            # Let run for 120 min

            # repeat untill all tracks used


a = GreedyAlgo()

