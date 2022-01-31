import matplotlib.pyplot as plt
from code.algorithmRunner.algorunner import *
from code.algorithmRunner.greedyrunner import GreedyRunner

# Runs the random algorithm
RunsRandom = AlgoRunner(1000)
RunsGreedy = GreedyRunner(1000)
# Stores all the seperate runs
box_data = RunsRandom.algo_samples

k_values = []

# Extracts the k_values for each run
for i in range(len(box_data)):

    k = box_data[i].get_k()
    # k = box_data[i].final_k()
    print(k)
    k_values.append(k)

# Saves the boxplot (More plots will be added with more algorithms)
plt.boxplot(k_values, patch_artist=True, labels=['random'])
plt.ylabel('k-values')
plt.savefig("plots/boxplot.png", format="png")
