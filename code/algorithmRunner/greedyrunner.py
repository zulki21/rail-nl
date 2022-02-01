from code.algorithms.greedyalgo import GreedyAlgo
import statistics


class GreedyRunner:
    def __init__(self, name_algo, sample_size) -> None:
        self.algo_samples = []

        for i in range(N):
            self.algo_samples.append(GreedyAlgo())

    def max_K(self):
        k_max = 0
        best_algo = None

        for algo in self.algo_samples:
            if algo.get_k() > k_max:
                k_max = algo.final_k()
                best_algo = algo

        return {best_algo: k_max}

    # function which returns mean median modus of dataset
    def stats(self):
        dataset = []
        for algo in self.algo_samples:
            dataset.append(algo.get_k())

        return {"mean": statistics.mean(dataset), "mode": statistics.mode(dataset), "median": statistics.median(dataset), "stdev": statistics.stdev(dataset), "max": max(dataset)}

    def histogram_greedy(self):
        dataset = []
        for algo in self.algo_samples:
            dataset.append(algo.get_k())
        return dataset
