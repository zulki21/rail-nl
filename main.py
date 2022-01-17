from loader import load_stations
from connection import Train
import random
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import csv
from visualize import get_route, get_all_routes


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


if __name__ == "__main__":
    stations = load_stations()

    trains = []

    # adding routes to the trains randomly
    for i in range(5):
        starting_station = random.choice(list(stations.values()))

        trains.append(Train(starting_station))

    for train in trains:
        current_station = train.get_route()[0]
        for i in range(5):
            connections = list(current_station.get_connections().keys())
            next_station = random.choice(connections)
            if train.get_time_route() + current_station.get_time(next_station) < 120:

                train.add_station(next_station)
                current_station = next_station

    a = unique_total_connections(trains)

    min = total_time_trains(trains)

    K = 10000 * (a / len(stations)) - (len(trains) * 100 - min)

    get_route(trains)
    get_all_routes(trains)

print("------------")
print(K)

with open('output_file', 'w') as f:

    writer = csv.writer(f)

    headers = ["trains", "stations"]
    writer.writerow(headers)

    for train in trains:

        route = []

        for i in range(len(train.get_route())):

            route.append(train.get_route()[i]._city_name)

        writer.writerow(route)

    score = ["SCORE = ", K]
    writer.writerow(score)
