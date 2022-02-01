from code.mainCode.loader import load_stations
import random
from code.mainCode.connection import Train


def unique_connection_train(train):
    """
    finds all unique connections of this train

    Parameters
    ----------
    train: train object
        will look at route of train
    Returns
    ------
    list of lists
        contains unique combination of every connection in route
    """

    pairs = []
    i = 0
    route = train.get_route()

    for i in range((len(route) - 1)):
        pairs.append([route[i].get_name(), route[i + 1].get_name()])

    unique_pairs = []
    for pair in pairs:
        unique_pairs.append(sorted(pair))

    b_set = set(tuple(x) for x in unique_pairs)
    b = [list(x) for x in b_set]

    return b


def unique_total_connections(list_of_trains):
    """
    finds all unique connections of all trains

    Parameters
    ----------
    train: train object
        will look at route of train
    Returns
    ------
    list of lists
        contains unique combination of every connection in route
    """
    unique_pairs = []

    combis = []
    for train in list_of_trains:
        abc = unique_connection_train(train)
        combis.extend(abc)

    for pair in combis:
        unique_pairs.append(sorted(pair))

    b_set = set(tuple(x) for x in unique_pairs)
    b = [list(x) for x in b_set]

    return len(b)


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


class RandomAlgo:
    def __init__(self, region) -> None:
        self.region = region
        self.stations = load_stations(self.region)
        self.trains = []
        self.used_connections = []
        self.all_connections = []

        if self.region == 1:
            self.number_connection = 28
            self.max_time = 120
            self.max_trains = 7
        elif self.region == 2:
            self.number_connection = 89
            self.max_time = 180
            self.max_trains = 20

        # creates object with all connections
        for station in self.stations.values():
            for connection in list(station.connections.keys()):
                if check_if_contains(self.all_connections, {station, connection}) == False:
                    self.all_connections.append({station, connection})

        # adding routes to the trains randomly
        for i in range(random.randint(0, self.max_trains - 1)):
            starting_station = random.choice(list(self.stations.values()))

            self.trains.append(Train(starting_station))

        for train in self.trains:
            current_station = train.get_route()[0]
            while train.get_time_route() <= self.max_time:

                connections = list(current_station.get_connections().keys())
                potential_connections = []

                for next_station in connections:
                    if check_if_contains(self.used_connections, {current_station, next_station}) == False:
                        potential_connections.append(next_station)

                if len(potential_connections) != 0:
                    next_station = random.choice(potential_connections)
                else:
                    next_station = random.choice(connections)

                if train.get_time_route() + current_station.get_time(next_station) > self.max_time:
                    break
                train.add_station(next_station)
                if check_if_contains(self.used_connections, {current_station, next_station}) == False:
                    self.used_connections.append(
                        {current_station, next_station})
                current_station = next_station

        first_tuple_list = [tuple(lst) for lst in self.all_connections]
        secnd_tuple_list = [tuple(lst) for lst in self.used_connections]

        first_set = set(first_tuple_list)
        secnd_set = set(secnd_tuple_list)
        diff = first_set.symmetric_difference(secnd_set)

        while len(diff) > 0 and len(self.trains) < self.max_trains:
            starting_station = random.sample(diff, 1)[0][0]
            self.trains.append(Train(starting_station))
            train = self.trains[-1]
            current_station = train.get_route()[0]
            while train.get_time_route() < 180:

                connections = list(current_station.get_connections().keys())
                potential_connections = []

                for next_station in connections:
                    if check_if_contains(self.used_connections, {current_station, next_station}) == False:
                        potential_connections.append(next_station)

                if len(potential_connections) != 0:
                    next_station = random.choice(potential_connections)
                else:
                    next_station = random.choice(connections)

                if train.get_time_route() + current_station.get_time(next_station) > 180:
                    break

                train.add_station(next_station)
                if check_if_contains(self.used_connections, {current_station, next_station}) == False:
                    self.used_connections.append(
                        {current_station, next_station})
                current_station = next_station

            first_tuple_list = [tuple(lst) for lst in self.all_connections]
            secnd_tuple_list = [tuple(lst) for lst in self.used_connections]

            first_set = set(first_tuple_list)
            secnd_set = set(secnd_tuple_list)
            diff = first_set.symmetric_difference(secnd_set)

            if len(self.used_connections) != self.number_connection:
                self.reset()

    def reset(self):
        self.__init__(self.region)

    def get_k(self):
        # calculate k value of the given random run
        a = unique_total_connections(self.trains)

        min = total_time_trains(self.trains)

        K = 10000 * (a / self.number_connection) - \
            (len(self.trains) * 100 + min)
        return K

    def get_trains(self):
        return self.trains
