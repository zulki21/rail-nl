from algorunner import AlgoRunner
from randomalgo import RandomAlgo
from algorunner import AlgoRunner
from greedyrunner import GreedyRunner
from greedyalgo import *
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

    # Save histogram as a png
    plt.savefig('Histogram.svg')


def greedyHist():
    # Plot histogram
    plt.hist(b.histogram_greedy(), bins='auto')

    # Labels for the histogram
    plt.xlabel("K-values")
    plt.ylabel("Frequency")
    plt.title('Greedy Algorithm')

    # Save histogram as a png
    plt.savefig('Histogram-Greedy.svg')


def createTabelRandom():
    content = a.stats().items()
    print(content)
    print(tabulate(content, tablefmt="github"))


def createTabelGreedy():
    content = b.stats().items()
    print(content)
    print(tabulate(content, tablefmt="github"))


if __name__ in '__main__':
    a = AlgoRunner(100)

    b = GreedyRunner(100)

    # print(a.max_K())
    # print(a.stats())
    # print(a.barChart())

    greedyHist()
    # randomHist()
    # createTabelRandom()
    createTabelGreedy()
