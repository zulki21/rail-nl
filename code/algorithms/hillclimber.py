from code.algorithms.randomalgo import RandomAlgo
from code.mainCode.connection import Train
import random


def total_time_trains(trains):
    """
    returns total time of all the trains

    Parameters
    ----------
    trains: list of train objects

    Returns   
    ------
    int
        time in mintues
    """
    min = 0
    for train in trains:
        min += train.get_time_route()

    return min


def check_if_contains(all_connections, set):
    """
    checks if a particular connections exist in a list of connections

    Parameters
    ----------
    all_connections: list of sets
        a list of sets containing all connections as sets of 2 stations
    set: set
        a set containing 2 station objects
    Returns
    ------
    boolean
        returns true or false
    """
    if len(all_connections) == 0:
        return False
    else:
        for connection in all_connections:
            if set == connection:
                return True
    return False


class Hillclimber:
    def __init__(self, region, reset_bound) -> None:
        """
        A class used to represent a Station

        ...

        Attributes
        ----------
        region : int
            a integer which represent 2 regions Holland or Nationaal
        stations : dict of station objects
            dictionary containing station names and the object
        trains: list
            list containing train objects 
        used_connections : list of sets
            list which keeps track of used connections
        all_connections : list of sets
            list with all connections
        best_used_connections : list of sets
            list with best connections the algorithm has found during process
        best_trains : list of train object
            list of best trains it has found
        highest_k: int
            highest k value during process
        max_time: int
            integer which keeps track of maximum time a train may use
        max_trains : int
            maximum amount of trains total model can use
        mistake_counter : int
            keeps track of how many times algorithm has failed to produce better output
        Methods
        -------
        random_change()
            performs a random change on a random state space
        get_k()
            returns k value of a state space
        get_trains()
            returns list of trains
        """

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

        # check which region we are using change values accordingly
        if self.region == 1:
            self.number_connection = 28
            self.max_time = 120
            self.max_trains = 7
        elif self.region == 2:
            self.number_connection = 89
            self.max_time = 180
            self.max_trains = 20

        # keep algorithm running untill no improvement takes place after certain steps
        while self.mistake_counter < self.mistake_bound:
            # make small random change
            self.random_change()

            # store variables if we find higher k
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
        """
        applies a random change to a state space
        """

        # remove 3 trains
        self.trains.remove(random.choice(self.trains))
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

        # look for unused conncetions
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
            while train.get_time_route() < self.max_time:

                connections = list(current_station.get_connections().keys())
                potential_connections = []

                for next_station in connections:
                    if not check_if_contains(self.used_connections, {current_station, next_station}):
                        potential_connections.append(next_station)

                if len(potential_connections) != 0:
                    next_station = random.choice(potential_connections)
                else:
                    next_station = random.choice(connections)

                if train.get_time_route() + current_station.get_time(next_station) > self.max_time:
                    break

                train.add_station(next_station)
                if not check_if_contains(self.used_connections, {current_station, next_station}):
                    self.used_connections.append(
                        {current_station, next_station})
                current_station = next_station
            first_tuple_list = [tuple(lst) for lst in self.all_connections]
            secnd_tuple_list = [tuple(lst) for lst in self.used_connections]

            first_set = set(first_tuple_list)
            secnd_set = set(secnd_tuple_list)
            diff = first_set.symmetric_difference(secnd_set)

    def get_k(self):
        """
        returns k value for a given state space

        Returns
        -------
        int
            K-value
        """
        a = len(self.used_connections)
        min = total_time_trains(self.trains)
        K = 10000 * (a / self.number_connection) - \
            (len(self.trains) * 100 + min)
        return K


    def get_trains(self):
        """
        returns list of trains

        Returns
        -------
        list
            list of trains object
        """
        return self.trains
