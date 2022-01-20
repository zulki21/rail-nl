import matplotlib.pyplot as plt
from algorunner import *

Runs = AlgoRunner(1000)

box_data = Runs.algo_samples

k_values = []

for i in range(len(box_data)):
    
    k = box_data[i].get_k()
    k_values.append(k)

plt.boxplot(k_values,patch_artist=True,labels=['random'])
plt.savefig("boxplot.png", format = "png")

