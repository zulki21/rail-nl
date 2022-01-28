from sqlite3 import DataError
from code.algorithms.randomalgo import RandomAlgo
import statistics


class AlgoRunner:
    def __init__(self, N) -> None:
        self.algo_samples = []

        for i in range(N):
            self.algo_samples.append(RandomAlgo())

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

        return {"mean": statistics.mean(dataset), "mode": statistics.mode(dataset), "median": statistics.median(dataset), "stdev": statistics.stdev(dataset), "max": max(dataset)}

    def histogram_random(self):
        dataset = []
        for algo in self.algo_samples:
            dataset.append(algo.get_k())
        return dataset
