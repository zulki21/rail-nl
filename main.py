from code.mainCode.loader import load_stations
from code.mainCode.connection import Train
import random
import csv
import numpy as np
import matplotlib.pyplot as plt
import argparse
from code.algorithmRunner.hillclimberrunner import AlgoRunnerHill
from code.algorithms.greedyalgo import GreedyAlgo
from code.visualization.visualize import visualize_histogram, visualize_boxplot, create_tabel


from code.visualization.visualize import *
from code.algorithmRunner.algorunner import AlgoRunner
from code.algorithms.randomalgo import RandomAlgo
from code.algorithmRunner.greedyrunner import GreedyRunner


# def main(area, duration, lines, algorithm):


if __name__ in '__main__':

    parser = argparse.ArgumentParser(description='RailNL')
    parser.add_argument('region', type=int, choices=[
                        1, 2], help='Holland ,National')
    parser.add_argument('algo', type=int, choices=[1, 2, 3, 4, 5],
                        help=('''
                            1: Random
                            2: Greedy
                            3: Hillclimber(Need to specify bound_climber)
                            4: Alterantive Hillclimber(Need to specify bound_climber)
                            5: All Algorithms(Need to specify bound_climber)
                            '''))
    parser.add_argument('sample_size', type=int,
                        default=50, help="choose the sample size for preferred algorithm")
    parser.add_argument('-bound_climber', type=int, default=500,
                        help="allowed mistake count before restart hillclimber algorithm")
    args = parser.parse_args()

    stations = load_stations(args.region)

    if args.algo == 5:
        all_algos = []
        all_algos.append(AlgoRunner(
            1, args.sample_size, args.region, args.bound_climber))
        all_algos.append(AlgoRunner(
            2, args.sample_size, args.region, args.bound_climber))
        all_algos.append(AlgoRunner(
            3, args.sample_size, args.region, args.bound_climber))
        all_algos.append(AlgoRunner(
            4, args.sample_size, args.region, args.bound_climber))
    else:
        list_of_algos = AlgoRunner(
            args.algo, args.sample_size, args.region, args.bound_climber)

    if args.region == 1 and args.algo == 1:
        output_file_hist = 'plots/histograms/histogram_Random_Holland.png'
        output_file_box = 'plots/boxplots/boxplot_Random_Holland.png'
        output_csv = 'output_files/Random_Holland.csv'

    elif args.region == 2 and args.algo == 1:
        output_file_hist = 'plots/histograms/histogram_Random_Nationaal.png'
        output_file_box = 'plots/boxplots/boxplot_Random_Nationaal.png'
        output_csv = 'output_files/Random_Nationaal.csv'

    elif args.region == 1 and args.algo == 2:
        output_file_hist = 'plots/histograms/histogram_Greedy_Holland.png'
        output_file_box = 'plots/boxplots/boxplot_Greedy_Holland.png'
        output_csv = 'output_files/Greedy_Holland.csv'

    elif args.region == 2 and args.algo == 2:
        output_file_hist = 'plots/histograms/histogram_Greedy_Nationaal.png'
        output_file_box = 'plots/boxplots/boxplot_Greedy_Nationaal.png'
        output_csv = 'output_files/Greedy_Nationaal.csv'

    elif args.region == 1 and args.algo == 3:
        output_file_hist = 'plots/histograms/histogram_Hillclimber_Holland.png'
        output_file_box = 'plots/boxplots/boxplot_Hillclimber_Holland.png'
        output_csv = 'output_files/Hillclimber_Holland.csv'

    elif args.region == 2 and args.algo == 3:
        output_file_hist = 'plots/histograms/histogram_Hillclimber_Nationaal.png'
        output_file_box = 'plots/boxplots/boxplot_Hillclimber_Nationaal.png'
        output_csv = 'output_files/Hillclimber_Nationaal.csv'

    elif args.region == 1 and args.algo == 4:
        output_file_hist = 'plots/histograms/histogram_Hillclimber-alt_Holland.png'
        output_file_box = 'plots/boxplots/boxplot_Hillclimber-alt_Holland.png'
        output_csv = 'output_files/Hillclimber-alt_Holland.csv'

    elif args.region == 2 and args.algo == 4:
        output_file_hist = 'plots/histograms/histogram_Hillclimber-alt_Nationaal.png'
        output_file_box = 'plots/boxplots/boxplot_Hillclimber-alt_Nationaal.png'
        output_csv = 'output_files/Hillclimber-alt_Nationaal.csv'

    elif args.region == 1 and args.algo == 5:
        output_file_hist = 'plots/histograms/histogram_Comparison_Holland.png'
        output_file_box = 'plots/boxplots/boxplot_Comparison_Holland.png'
        visualize_histogram(all_algos, output_file_hist)
        visualize_boxplot(all_algos, output_file_box)

    elif args.region == 2 and args.algo == 5:
        output_file_hist = 'plots/histograms/histogram_Comparison_Nationaal.png'
        output_file_box = 'plots/boxplots/boxplot_Comparison_Nationaal.png'
        visualize_histogram(all_algos, output_file_hist)
        visualize_boxplot(all_algos, output_file_box)

    # visualize_histogram(list_of_algos, output_file_hist)
    # visualize_boxplot(list_of_algos, output_file_box)
    # create_tabel(list_of_algos)

    # get_all_stations(stations)
    # visualize_all_routes(trains, stations)

    best = list(list_of_algos.max_K().keys())[0]
    trains = best.get_trains()

    with open(output_csv, 'w') as f:

        writer = csv.writer(f)

        headers = ["trains", "stations"]
        writer.writerow(headers)

        train_number = 1
        for train in trains:

            route = []

            for i in range(len(train.get_route())):

                route.append(train.get_route()[i]._city_name)

            train_route = [f'train_{train_number}: {route}']
            writer.writerow(train_route)
            train_number += 1

        score = [f'SCORE = {best}']
        writer.writerow(score)
