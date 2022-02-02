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
    parser.add_argument('bound_climber', type=int, default=500,
                        help="allowed mistake count before restart hillclimber algorithm")
    args = parser.parse_args()

    stations = load_stations(args.region)

    algos = []
    if args.algo == 5:
        algos.append(AlgoRunner(
            1, args.sample_size, args.region, args.bound_climber))
        algos.append(AlgoRunner(
            2, args.sample_size, args.region, args.bound_climber))
        algos.append(AlgoRunner(
            3, args.sample_size, args.region, args.bound_climber))
        algos.append(AlgoRunner(
            4, args.sample_size, args.region, args.bound_climber))
    else:
        algos.append(AlgoRunner(
            args.algo, args.sample_size, args.region, args.bound_climber))

    algo_names = {
        1: 'Random',
        2: 'Greedy',
        3: 'Hillclimber',
        4: 'Hillclimber_alt',
        5: 'Comparison'
    }

    region_names = {
        1: 'Holland',
        2: 'Nationaal'
    }

    output_file_hist = f'plots/histograms/histogram_{algo_names[args.algo]}_{region_names[args.region]}.png'
    output_file_box = f'plots/boxplots/boxplot_{algo_names[args.algo]}_{region_names[args.region]}.png'
    title = f'{algo_names[args.algo]} Algorithm {region_names[args.region]}'
    label = [f'{algo_names[args.algo]}-{region_names[args.region]}']
    output_csv = f'output_files/{algo_names[args.algo]}_{region_names[args.region]}.csv'

    if args.algo == 5:
        label = list(algo_names.values())

    #     output_file_hist = 'plots/histograms/histogram_Comparison_Holland.png'
    #     output_file_box = 'plots/boxplots/boxplot_Comparison_Holland.png'
    #     combine_boxplots(all_algos, output_file_box)

    # elif args.region == 2 and args.algo == 5:
    #     output_file_hist = 'plots/histograms/histogram_Comparison_Nationaal.png'
    #     output_file_box = 'plots/boxplots/boxplot_Comparison_Nationaal.png'
    #     combine_boxplots(all_algos, output_file_box)

    visualize_histogram(algos, output_file_hist, title, label)
    visualize_boxplot(algos, output_file_box, label)
    create_tabel(algos)

    if args.algo == 5:
        exit()

    best = list(algos[0].max_K().keys())[0]
    trains = best.get_trains()

    get_all_stations(stations)
    visualize_all_routes(trains, stations)

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
