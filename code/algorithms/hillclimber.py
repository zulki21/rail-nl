from pyrsistent import b
from code.algorithms.randomalgo import RandomAlgo
from code.mainCode.connection import Train
import random

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

        temp_trains = self.trains
        temp_used_connections = self.all_connections

        self.mistake_counter = 0

        while self.mistake_counter != 1:
            #Doe een kleine random aanpassing
            self.random_change()
        
            # Als staat verslechterd:
            if self.highest_k > self.get_k():
                # Maak aanpassing ongedaan
                self.trains = temp_trains
                self.used_connections = temp_used_connections
                self.mistake_counter += 1
            else:
                self.highest_k = self.get_k()
                self.mistake_counter = 0
                temp_trains = self.trains
                temp_used_connections = self.used_connections




    def get_k(self):
        # calculate k value of the given random run
        a = unique_total_connections(self.trains)

        min = total_time_trains(self.trains)

        K = 10000 * (a / 89) - (len(self.trains) * 100 + min)

        return K


    def random_change(self):
        # train we want to change
        train = random.choice(self.trains) 

        # delete train
        self.trains.remove(train)

        
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


        first_tuple_list = [tuple(lst) for lst in self.all_connections]
        secnd_tuple_list = [tuple(lst) for lst in self.used_connections]

        first_set = set(first_tuple_list)
        secnd_set = set(secnd_tuple_list)
        diff = first_set.symmetric_difference(secnd_set)

        while len(diff) > 0 and len(self.trains) < 20:
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
