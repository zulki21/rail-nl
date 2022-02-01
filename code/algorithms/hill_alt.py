from pyrsistent import b
from code.algorithms.randomalgo import RandomAlgo
from code.mainCode.connection import Train
import random


def total_time_trains(trains):
    min = 0
    for train in trains:
        min += train.get_time_route()

    return min


def check_if_contains(all_connections, set):
    if len(all_connections) == 0:
        return False
    else:
        for connection in all_connections:
            if set == connection:
                return True
    return False


class Hillclimber:
    def __init__(self, region, reset_bound) -> None:

        # Run randomalgo for a random state
        a = RandomAlgo(region)
        self.region = region
        self.mistake_bound = reset_bound
        self.stations = a.stations
        self.trains = a.trains
        self.used_connections = a.used_connections
        self.all_connections = a.all_connections
        self.unused_connections = list(set([frozenset(
            i) for i in self.all_connections]) - set([frozenset(i) for i in self.used_connections]))

        self.best_used_connections = a.used_connections[:]
        self.best_trains = a.trains[:]
        self.highest_k = a.get_k()

        self.mistake_counter = 0

        if self.region == 1:
            self.number_connection = 28
            self.max_time = 120
            self.max_trains = 7
        elif self.region == 2:
            self.number_connection = 89
            self.max_time = 180
            self.max_trains = 20

        while self.mistake_counter < self.mistake_bound:

            self.random_change()

            if self.get_k() > self.highest_k:
                self.mistake_counter = 0
                self.best_used_connections = self.used_connections[:]
                self.best_trains = self.trains[:]
                self.highest_k = self.get_k()
            else:
                self.used_connections = self.best_used_connections[:]
                self.trains = self.best_trains[:]
                self.mistake_counter += 1

    def random_change(self):
        # train we want to change
        train = random.choice(self.trains)
        # delete train
        self.trains.remove(train)
        self.trains.remove(random.choice(self.trains))
        self.trains.remove(random.choice(self.trains))

        # recalculate used connections

        unique_pairs_alpha = []

        combis = []
        for train in self.trains:
            pairs = []
            i = 0
            route = train.get_route()

            for i in range((len(route) - 1)):
                pairs.append([route[i], route[i + 1]])

            unique_pairs = []
            for pair in pairs:

                unique_pairs.append(pair)

            b_set = set(tuple(x) for x in unique_pairs)
            abc = [list(x) for x in b_set]

            combis.extend(abc)
        for pair in combis:
            unique_pairs_alpha.append(pair)

        b_set = list(set(x) for x in unique_pairs_alpha)
        b_set = list(set(frozenset(item) for item in b_set))
        b_set = [set(item) for item in set(frozenset(item) for item in b_set)]

        self.used_connections = b_set

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

                # lets each train run one at a time
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

                            if k > best_k:
                                best_k = k
                                next_station = connection

                            avaliable_routes += 1

                    if avaliable_routes == 0:
                        break

                    elif len(current_train.get_route()) > 2 and next_station == current_train.get_route()[-2]:
                        break

                    elif {current_station, next_station} not in self.used_connections:
                        self.used_connections.append(
                            {current_station, next_station})
                    current_train.add_station(next_station)

    def get_k(self):
        # calculate k value of the given random run
        a = len(self.used_connections)
        min = total_time_trains(self.trains)
        K = 10000 * (a / self.number_connection) - \
            (len(self.trains) * 100 + min)
        return K

    def get_unused(self):
        return list(set([frozenset(i) for i in self.all_connections]) - set([frozenset(i) for i in self.used_connections]))

    def get_trains(self):
        return self.trains
