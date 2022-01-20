from algorunner import AlgoRunner
from randomalgo import RandomAlgo
from algorunner import AlgoRunner
import matplotlib.pyplot as plt
import numpy as np


def plotBar():

    # Create figure
    # plt.figure(figsize=(20, 10), dpi=80)

    # Adding data
    x_axis = a.barChart()
    y_axis = list(map(str, list(range(len(x_axis)))))
    y_pos = np.arange(len(y_axis))

    # Create bars
    plt.barh(y_pos, x_axis)

    # N on the x-axis with a frequency of 25
    plt.yticks(np.arange(0, len(y_axis)+1, 25))
    # plt.xticks(np.arange(8000, len(x_axis)+1, 100))

    plt.xlim([8000, 9000])

    # Labels for the graph
    plt.xlabel("K-value")
    plt.ylabel("Frequency")

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
