from algorunner import AlgoRunner
from randomalgo import RandomAlgo
from algorunner import AlgoRunner
import matplotlib.pyplot as plt
import numpy as np


def plotBar():

    # Create figure
    # plt.figure(figsize=(20, 10), dpi=80)

    # Adding data
    height = a.barChart()
    bars = list(map(str, list(range(len(height)))))
    y_pos = np.arange(len(bars))

    # Create bars
    plt.barh(height, y_pos)

    # N on the x-axis with a frequency of 25
    plt.xticks(np.arange(0, len(bars)+1, 25))

    # Labels for the graph
    plt.xlabel("K-waarden")
    plt.ylabel("N")

    # plt.gca().invert_xaxis()

    # Show and save graphic
    plt.show()
    plt.savefig('barChart.png')


if __name__ in '__main__':
    a = AlgoRunner(100)

    print(a.max_K())
    print(a.stats())
    print(a.barChart())

    plotBar()
