import numpy as np
import matplotlib.pyplot as plt
from code.algorithmRunner.algorunner import AlgoRunner
from code.algorithmRunner.hillclimberrunner import AlgoRunnerHill
from code.algorithms.randomalgo import RandomAlgo
from code.algorithmRunner.greedyrunner import GreedyRunner
from code.algorithms.greedyalgo import GreedyAlgo

from code.visualization.visualize import visualize_boxplot_Random, visualize_boxplot_Greedy, randomHist, greedyHist, createTabelGreedy, createTabelRandom, hillclimberHist, createTabelHillclimber, visualize_boxplot_Hillclimber


if __name__ in '__main__':
    # visualize_boxplot_Random()
    # visualize_boxplot_Greedy()
    visualize_boxplot_Hillclimber()
    # greedyHist()
    # randomHist()
    hillclimberHist()
    # createTabelRandom()
    # createTabelGreedy()
    createTabelHillclimber()
