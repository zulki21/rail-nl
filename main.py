from loader import load_stations
from connection import Train
import random
import csv
from visualize import *
from algorunner import AlgoRunner
from randomalgo import RandomAlgo


if __name__ in '__main__':
    a = AlgoRunner(500)
    print(list(a.max_K().keys())[0])
    best = list(a.max_K().keys())[0]

    trains = best.get_trains()
    c = []
    for train in trains:
       
        b = []
        for station in train.get_route():
            b.append(station.get_name())

        c.append(b)

    i = 1
    for traject in c:
        print(f"trein{i} : {traject}")
        i+= 1


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
