from tabnanny import check
from code.mainCode.loader import load_stations
import random
from code.mainCode.connection import Train



def k_value(trains, used_connections, minutes, region):
    """
    Finds the k value for a given route
    """

    if region == 1:

        return 10000 * (used_connections / 28) - (trains * 100 + minutes)

    if region == 2:

        return 10000 * (used_connections / 89) - (trains * 100 + minutes)


def total_time_trains(trains):
    """
    Calculates the total time taken by all the trains
    """
    min = 0

    for train in trains:

        min += train.get_time_route()

    return min


class GreedyAlgo:
    
    def __init__(self, region):
        """
        This function runs a greedy algorithm, for every step the train takes it calculates the best
        route based on which connection gives the best k_value at that moment
        """
        self.region = region
        self.stations = load_stations(region)
        self.trains = []
        self.used_connections = []

        # The parameters are based on which region the trains are driving in
        if region == 1:

            self.number_connection = 28
            self.max_time = 120
            self.max_trains = 7

        elif region == 2:

            self.number_connection = 89
            self.max_time = 180
            self.max_trains = 20

        # Runs the algorithm untill all connections are used or the max amount of trains is reached
        while len(self.used_connections) != self.number_connection and len(self.trains) < self.max_trains:

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

            # lets each train run one at a time untill its reached its max time
            current_train = Train(random.choice(list(possible_start)))
            self.trains.append(current_train)

            while current_train.get_time_route() < self.max_time and len(self.used_connections) != self.number_connection:

                current_station = current_train.get_route()[-1]

                connections = current_station.connections

                # decides which route to go based off which one has the highest k value
                best_k = -10000000
                avaliable_routes = 0
                for connection in connections:

                    if current_train.get_time_route() + current_station.get_time(connection) <= self.max_time:

                        if {current_station, connection} not in self.used_connections:
                            k = k_value(len(self.trains), (len(self.used_connections) + 1),
                                        total_time_trains(self.trains) + connection.get_time(current_station), self.region)
                        else:
                            k = k_value(len(self.trains), (len(self.used_connections)), total_time_trains(
                                self.trains) + connection.get_time(current_station), self.region)

                        # Choses the best connection based on the k value
                        if k > best_k:
                            best_k = k
                            next_station = connection

                        avaliable_routes += 1

                # If all of the routes makes the train go over the time limit it stops
                if avaliable_routes == 0:

                    break

                # If a train returns to the station it was at before, it stops the route
                elif len(current_train.get_route()) > 2 and next_station == current_train.get_route()[-2]:
                    break

                # If an unused connection is used it is saved
                elif {current_station, next_station} not in self.used_connections:
                    self.used_connections.append(
                        {current_station, next_station})

                current_train.add_station(next_station)

    def get_k(self):
        """
        Allows the final k_value to be saved
        """
        return 10000 * (len(self.used_connections) / self.number_connection) - (len(self.trains) * 100 + total_time_trains(self.trains))

    def get_trains(self):
        """
        Returns a list of the trains used
        """
        return self.trains
