import numpy as np
import matplotlib.pyplot as plt
from code.algorithmRunner.algorunner import AlgoRunner
from code.algorithms.randomalgo import RandomAlgo
from code.algorithmRunner.greedyrunner import GreedyRunner
from code.algorithms.greedyalgo import *
from code.visualization.visualize import visualize_boxplot_Random, visualize_boxplot_Greedy, randomHist, greedyHist, createTabelGreedy, createTabelRandom


if __name__ in '__main__':
    # visualize_boxplot_Random()
    # visualize_boxplot_Greedy()
    # greedyHist()
    # randomHist()
    createTabelRandom()
    createTabelGreedy()
