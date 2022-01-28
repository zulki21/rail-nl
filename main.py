from code.mainCode.loader import load_stations
from code.mainCode.connection import Train
import random
import csv
from code.visualization.visualize import *
from code.algorithmRunner.algorunner import AlgoRunner
from code.algorithms.randomalgo import RandomAlgo
from code.algorithmRunner.greedyrunner import GreedyRunner
import argparse


def main(area, duration, lines, algorithm):

    if __name__ in '__main__':
        stations = load_stations()

        a = AlgoRunner(100)
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

    # Set-up parsing command line arguments
        parser = argparse.ArgumentParser(
            description="Run program with required and optional arguments")

        # Adding arguments
        parser.add_argument("-a", "--area",
                            help="Area run the algorithms")
        parser.add_argument("-d", "--duration",
                            help="Max duration for one line")
        parser.add_argument("-L", "--lines", help="Max number of lines")
        parser.add_argument("-A", "--algorithm", help="Algorithms to run")
        parser.add_argument("-h", "--help", help="Prints this message")
        parser.add_argument("-r", "--repeat", help="Number of repetions")
        parser.add_argument("-i", "--iterations",
                            help="Number of iterations per run")

        # Read arguments from command line
        args = parser.parse_args()

        # Run main with provide arguments
        main(args.area, args.duration, args.lines, args.algorithm)
