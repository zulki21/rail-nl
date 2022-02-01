from code.algorithms.randomalgo import RandomAlgo
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.greedyalgo import GreedyAlgo
from code.algorithms.hill_alt import Hillclimber_alt
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
                print(f" {100 * i/self.N} % completed", end="\r",flush=True)

        elif algorithm == 2:
            # greedy
            for i in range(1, 1 + self.N):
                self.algo_samples.append(GreedyAlgo(region))
                print(f" {100 * i/self.N} % completed", end="\r",flush=True)
        elif algorithm == 3:
            # hillclimber
            for i in range(self.N):
                self.algo_samples.append(Hillclimber(region, reset_bound))
                print(f" {100 * i/self.N} % completed", end="\r",flush=True)
        elif algorithm == 4:
            # alternative hillclimber
            for i in range(self.N):
                self.algo_samples.append(Hillclimber_alt(region, reset_bound))
                print(f" {100 * i/self.N} % completed", end="\r",flush=True)

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
