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


class RandomAlgo:
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
    max_time: int
        integer which keeps track of maximum time a train may use
    max_trains : int
        maximum amount of trains total model can use

    Methods
    -------
    reset()
        reinitializes object if it doesn't give desired outcome needed for lower bias
    get_k()
        returns k of a given model
    get_trains()
        returns trains in a given model
    """
    def __init__(self, region) -> None:
        self.region = region
        self.stations = load_stations(self.region)
        self.trains = []
        self.used_connections = []
        self.all_connections = []

        # check which map has been used and change magic numbers to desired ones
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

        # adding random amount of trains
        for i in range(random.randint(0, self.max_trains - 1)):
            starting_station = random.choice(list(self.stations.values()))

            self.trains.append(Train(starting_station))

        # start adding routes to trains
        for train in self.trains:
            current_station = train.get_route()[0]
            while train.get_time_route() <= self.max_time:

                connections = list(current_station.get_connections().keys())
                potential_connections = []

                # prefer non used stations over stations which are not used 
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

        # check if all connections are used
        first_tuple_list = [tuple(lst) for lst in self.all_connections]
        secnd_tuple_list = [tuple(lst) for lst in self.used_connections]

        first_set = set(first_tuple_list)
        secnd_set = set(secnd_tuple_list)
        diff = first_set.symmetric_difference(secnd_set)

        # keep adding trains till we have used all connections
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

                # if time of train goes over desired max time stop adding to route
                if train.get_time_route() + current_station.get_time(next_station) > 180:
                    break

                train.add_station(next_station)
                if check_if_contains(self.used_connections, {current_station, next_station}) == False:
                    self.used_connections.append(
                        {current_station, next_station})
                current_station = next_station
            
            # check if all connections are used
            first_tuple_list = [tuple(lst) for lst in self.all_connections]
            secnd_tuple_list = [tuple(lst) for lst in self.used_connections]

            first_set = set(first_tuple_list)
            secnd_set = set(secnd_tuple_list)
            diff = first_set.symmetric_difference(secnd_set)

            # if not all connections are used start proccess again
            if len(self.used_connections) != self.number_connection:
                self.reset()

    def reset(self):
        """
        reruns the object
        """
        self.__init__(self.region)

    def get_k(self):
        """
        returns K

        Returns
        -------
        int
            K-value
        """
        a = unique_total_connections(self.trains)

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
            list of train objects
        """
        return self.trains
