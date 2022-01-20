from loader import load_stations
import random
from connection import Train

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

class RandomAlgo:
    def __init__(self) -> None:
        self.stations = load_stations()

        self.trains = []

    # adding routes to the trains randomly
        for i in range(random.randint(0,100)):
            starting_station = random.choice(list(self.stations.values()))

            self.trains.append(Train(starting_station))

        for train in self.trains:
            current_station = train.get_route()[0]
            random_num = random.randint(0, 120)
            while train.get_time_route() < random_num:
                connections = list(current_station.get_connections().keys())
                next_station = random.choice(connections)
                train.add_station(next_station)
                current_station = next_station
    
    def get_k(self):
        # calculate k value of the given random run
        a = unique_total_connections(self.trains)

        min = total_time_trains(self.trains)

        K = 10000 * (a / 89) - (len(self.trains) * 100 + min)
        return K



