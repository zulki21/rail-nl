from algorunner import AlgoRunner
from randomalgo import RandomAlgo
from algorunner import AlgoRunner
import matplotlib.pyplot as plt
import numpy as np


def plotBar():
    plt.figure(figsize=(20, 10), dpi=80)

    # Make a random dataset:
    height = a.barChart()
    bars = list(map(str, list(range(len(height)))))
    y_pos = np.arange(len(bars))

    # Create bars
    plt.bar(y_pos, height, width=0.9)

    # Create names on the x-axis
    plt.xticks(np.arange(0, len(bars)+1, 25))

    plt.gca().invert_yaxis()

    # Show graphic
    plt.show()
    plt.savefig('barChart.png')


if __name__ in '__main__':
    a = AlgoRunner(100)

    print(a.max_K())
    print(a.stats())

    plotBar()
