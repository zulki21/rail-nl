from code.algorithmRunner.algorunner import AlgoRunner
from code.algorithmRunner.hillclimberrunner import AlgoRunnerHill
from code.algorithms.randomalgo import RandomAlgo
from code.algorithmRunner.greedyrunner import GreedyRunner
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


def randomHist():

    # Plot histogram
    plt.hist(a.histogram_random(), bins='auto')

    # Labels for the histogram
    plt.xlabel("K-values")
    plt.ylabel("Frequency")
    plt.title('Random Algorithm')
    # plt.legend(['Greedy', 'Random'])

    # Save histogram as a png
    plt.savefig('plots/Histogram.png')


def greedyHist():
    # Plot histogram
    plt.hist(b.histogram_greedy(), bins='auto')

    # Labels for the histogram
    plt.xlabel("K-values")
    plt.ylabel("Frequency")
    plt.title('Greedy Algorithm')

    # Save histogram as a png
    plt.savefig('plots/Histogram-Greedy.png')


def createTabelRandom():
    content = a.stats().items()
    print(content)
    print(tabulate(content, tablefmt="github"))


def createTabelGreedy():
    content = b.stats().items()
    print(content)
    print(tabulate(content, tablefmt="github"))


if __name__ in '__main__':
    a = AlgoRunnerHill(100)

    # b = GreedyRunner(100)

    # print(a.max_K())
    # print(a.stats())
    # print(a.barChart())

    # greedyHist()
    # randomHist()

    createTabelRandom()
    # createTabelGreedy()
