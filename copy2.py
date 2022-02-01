from tabnanny import check
from code.mainCode.loader import load_stations
import random
from code.mainCode.connection import Train


def get_k(trains, used_connections, minutes):

    return 10000 * (used_connections / 89) - (trains * 100 + minutes)


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

        while len(self.used_connections) != 89 and len(self.trains) < 20:

            # chooses a starting station based off which one still has untravelled connections
            possible_start = []

            for station in self.stations.values():

                station_connections = station.connections

                points = 0
                for connection in station_connections:

                    if {station, connection} in self.used_connections:

                        points += 1

                if points != len(station_connections):

                    possible_start.append(station)

            # lets each train run one at a time
            current_train = Train(random.choice(list(possible_start)))
            self.trains.append(current_train)

            while current_train.get_time_route() < 180 and len(self.used_connections) != 89:

                current_station = current_train.get_route()[-1]

                connections = current_station.connections

                # decides which route to go based off which one has the highest k value
                best_k = -10000000
                avaliable_routes = 0
                for connection in connections:

                    if current_train.get_time_route() + current_station.get_time(connection) <= 180:

                        if {current_station, connection} not in self.used_connections:
                            k = get_k(len(self.trains), (len(self.used_connections) + 1),
                                      total_time_trains(self.trains) + connection.get_time(current_station))
                        else:
                            k = get_k(len(self.trains), (len(self.used_connections)), total_time_trains(
                                self.trains) + connection.get_time(current_station))

                        if k > best_k:
                            best_k = k
                            next_station = connection

                        avaliable_routes += 1

                if avaliable_routes == 0:
                    break

                elif {current_station, next_station} not in self.used_connections:
                    self.used_connections.append(
                        {current_station, next_station})
                current_train.add_station(next_station)
        print(len(self.used_connections))
        print(len(self.trains))

    def final_k(self):

        return 10000 * (len(self.used_connections) / 89) - (len(self.trains) * 100 + total_time_trains(self.trains))

    def get_trains(self):
        return self.trains


a = GreedyAlgo()
print(a.final_k())