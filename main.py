from code.mainCode.loader import load_stations
from code.mainCode.connection import Train
import random
import csv
import numpy as np
import matplotlib.pyplot as plt
import argparse
from code.algorithmRunner.hillclimberrunner import AlgoRunnerHill
from code.algorithms.greedyalgo import GreedyAlgo
from code.visualization.visualize import visualize_histogram, visualize_boxplot
from code.visualization.visualize import createTabelGreedy, createTabelRandom, createTabelHillclimber

from code.visualization.visualize import *
from code.algorithmRunner.algorunner import AlgoRunner
from code.algorithms.randomalgo import RandomAlgo
from code.algorithmRunner.greedyrunner import GreedyRunner


# def main(area, duration, lines, algorithm):


if __name__ in '__main__':

    parser = argparse.ArgumentParser(description='RailNL')
    parser.add_argument('region', type=int, choices=[
                        1, 2], help='Holland ,National')
    parser.add_argument('algo', type=int, choices=[1, 2, 3],
                        help=('''
                            1: Random
                            2: Greedy
                            3: Hillclimber
                            '''))
    parser.add_argument('sample_size', type=int,
                        default=50, help="choose the sample size for preferred algorithm")
    parser.add_argument('bound_climber', type=int, default=500,
                        help="allowed mistake count before restart hillclimber algorithm")
    args = parser.parse_args()

    stations = load_stations(args.region)

    list_of_algos = AlgoRunner(
        args.algo, args.sample_size, args.region, args.bound_climber)

    if args.region == 1 and args.algo == 1:
        output_file_hist = 'plots/histograms/histogram_Random_Holland.png'
        output_file_box = 'plots/boxplots/boxplot_Random_Holland.png'
        visualize_histogram(list_of_algos, output_file_hist)
        visualize_boxplot(list_of_algos, output_file_box)

    # if args.region == 2 and args.algo == 1:
    #     output_file = 'plots/histogram_Random_Nationaal.png'
    #     histogram(list_of_algos, output_file)

    best = list(list_of_algos.max_K().keys())[0]
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

    visualize_boxplot(list_of_algos, output_file_box)

    visualize_histogram(list_of_algos, output_file_hist)

    createTabelRandom(list_of_algos)
    createTabelGreedy(list_of_algos)
    createTabelHillclimber(list_of_algos)

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
