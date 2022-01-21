from algorunner import AlgoRunner
from randomalgo import RandomAlgo
from algorunner import AlgoRunner
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


def plotHist():

    # Plot histogram
    plt.hist(a.barChart(), bins='auto')

    # Labels for the histogram
    plt.xlabel("K-values")
    plt.ylabel("Frequency")

    # Save histogram as a png
    plt.savefig('Histogram.png')


def createTabel():
    content = a.stats().items()
    print(content)
    print(tabulate(content, tablefmt="github"))


if __name__ in '__main__':
    a = AlgoRunner(100)

    print(a.max_K())
    print(a.stats())
    print(a.barChart())

    plotHist()
    createTabel()
