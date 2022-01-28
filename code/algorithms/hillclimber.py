from code.mainCode.loader import load_stations
from code.algorithms.randomalgo import RandomAlgo


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


class Hillclimber:
    def __init__(self) -> None:

        # Run randomalgo for a random state
        a = RandomAlgo()

        self.stations = a.stations
        self.trains = a.trains
        self.used_connections = a.used_connections
        self.all_connections = a.all_connections
        self.highest_k = a.get_k()

        self.temp_trains = self.trains
        self.temp_used_connections = self.all_connections

        self.mistake_counter = 0

        while self.mistake_counter != 50:

            # Doe een kleine random aanpassing
            # Wat voor aanpassingen zijn er mogelijk
            # Hele traject aanpassen beste denk ik
            
        
            # Als staat verslechterd:
            if self.highest_k > self.get_k():
                # Maak aanpassing ongedaan
                self.trains = self.temp_trains
                self.used_connections = self.temp_used_connections
        

    def get_k(self):
        # calculate k value of the given random run
        a = unique_total_connections(self.trains)

        min = total_time_trains(self.trains)

        K = 10000 * (a / 89) - (len(self.trains) * 100 + min)

        return K
