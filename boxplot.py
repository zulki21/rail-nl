import matplotlib.pyplot as plt
from algorunner import *
import numpy as np

# Runs the random algorithm
Runs = AlgoRunner(1000)

# Stores all the seperate runs
box_data = Runs.algo_samples

k_values = []

# Extracts the k_values for each run
for i in range(len(box_data)):

    k = box_data[i].get_k()
    print(k)
    k_values.append(k)

# Saves the boxplot (More plots will be added with more algorithms)
plt.boxplot(k_values, patch_artist=True, labels=['random'])
plt.savefig("boxplot.png", format="png")
