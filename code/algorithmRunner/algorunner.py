from code.algorithms.randomalgo import RandomAlgo
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.greedyalgo import GreedyAlgo
import statistics
import sys
sys.setrecursionlimit(10000)


class AlgoRunner:
    def __init__(self, algorithm, sample_size, region, reset_bound) -> None:
        self.algo_samples = []
        self.N = sample_size

        if algorithm == 1:
            for i in range(self.N):
                self.algo_samples.append(RandomAlgo(region=region))
                print(f"{i/self.N* 100} percent complete         \r")

        elif algorithm == 2:
            # greedy
            for i in range(1, 1 + self.N):
                self.algo_samples.append(GreedyAlgo(region))
                print(f"{i/self.N* 100} percent complete         \r")
        elif algorithm == 3:
            # hillclimber
            for i in range(self.N):
                self.algo_samples.append(Hillclimber(region, reset_bound))
                print(f"{i/self.N *100}%")

    def max_K(self):
        k_max = -10000
        best_algo = None

        for algo in self.algo_samples:
            if algo.get_k() > k_max:
                k_max = algo.get_k()
                best_algo = algo

        return {best_algo: k_max}

    # function which returns mean median modus of dataset
    def stats(self):
        dataset = []
        for algo in self.algo_samples:
            dataset.append(algo.get_k())

        return {"mean": statistics.mean(dataset), "mode": statistics.mode(dataset), "median": statistics.median(dataset), "stdev": statistics.stdev(dataset), "max": max(dataset), "min": min(dataset)}

    def histogram(self):
        dataset = []
        for algo in self.algo_samples:
            dataset.append(algo.get_k())
        return dataset
