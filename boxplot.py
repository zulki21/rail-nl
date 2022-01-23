import matplotlib.pyplot as plt
from algorunner import *
import numpy as np

Runs = AlgoRunner(1000)

box_data = Runs.algo_samples

k_values = []

for i in range(len(box_data)):

    k = box_data[i].get_k()
    k_values.append(k)

plt.boxplot(k_values, patch_artist=True, labels=['random'])
# plt.yticks(np.arange(8000, 9100, 100))
# plt.ylim([8000, 9000])
plt.savefig("boxplot.png", format="png")
