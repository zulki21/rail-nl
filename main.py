from code.mainCode.loader import load_stations
from code.mainCode.connection import Train
import random
import csv
from code.visualization.visualize import *
from code.algorithmRunner.algorunner import AlgoRunner
from code.algorithms.randomalgo import RandomAlgo
from code.algorithmRunner.greedyrunner import GreedyRunner


if __name__ in '__main__':
    stations = load_stations()

    a = AlgoRunner(500)
    # e = GreedyRunner(500)
    # print(list(a.max_K().keys())[0])
    # best = list(a.max_K().keys())[0]

    print(list(a.max_K().keys())[0])
    best = list(a.max_K().keys())[0]

    trains = best.get_trains()

    get_route(trains)
    c = []

    for train in trains:

        b = []

        for station in train.get_route():
            b.append(station.get_name())

        c.append(b)

    i = 1

    for traject in c:
        print(f"trein{i} : {traject}")
        i += 1

    get_all_stations(stations)
    visualize_all_routes(trains, stations)


# with open('output_file', 'w') as f:

#     writer = csv.writer(f)

#     headers = ["trains", "stations"]
#     writer.writerow(headers)

#     for train in trains:

#         route = []

#         for i in range(len(train.get_route())):

#             route.append(train.get_route()[i]._city_name)

#         writer.writerow(route)

#     score = ["SCORE = ", K]
#     writer.writerow(score)
