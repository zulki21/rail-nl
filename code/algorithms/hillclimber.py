from pyrsistent import b
from randomalgo import RandomAlgo
from connection import Train
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
    def __init__(self) -> None:

        # Run randomalgo for a random state
        a = RandomAlgo()

        self.stations = a.stations
        self.trains = a.trains
        self.used_connections = a.used_connections
        self.all_connections = a.all_connections
        self.unused_connections = list(set([frozenset(i) for i in self.all_connections]) - set([frozenset(i) for i in self.used_connections]))

        self.best_used_connections = a.used_connections[:]
        self.best_trains = a.trains[:]
        self.highest_k = a.get_k()
        
        self.mistake_counter = 0


        
        while self.mistake_counter < 10000:
            
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

            print(f"k-score :{self.get_k()}")
            
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

    
    def get_k(self):
        # calculate k value of the given random run
        a = len(self.used_connections)
        min = total_time_trains(self.trains)
        K = 10000 * (a / 89) - (len(self.trains) * 100 + min)
        return K

    def get_unused(self):
        return list(set([frozenset(i) for i in self.all_connections]) - set([frozenset(i) for i in self.used_connections]))