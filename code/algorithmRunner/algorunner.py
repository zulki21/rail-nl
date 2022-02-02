import time
from code.algorithms.randomalgo import RandomAlgo
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.greedyalgo import GreedyAlgo
from code.algorithms.hillclimber_greedy import Hillclimber_greedy
import statistics
import sys
sys.setrecursionlimit(10000)


class AlgoRunner:
    """
    A class used to run the algorithm multiple times and store it's data

    ...

    Attributes
    ----------
    algo_samples: list
        a list in which we have the results of multiple algorithms
    N: int
        Amount of samples we want from a given run
    Methods
    -------
    max_k(station)
        gives you the algorithm with the maximum k value
    stats()
        returns different stats about the algo samples
    histogram()
        used for the histogram of the k-values

    """

    def __init__(self, algorithm, sample_size, region, reset_bound) -> None:
        self.algo_samples = []
        self.N = sample_size

        if algorithm == 1:
            # random
            for i in range(self.N):
                self.algo_samples.append(RandomAlgo(region=region))
                print(f" {100 * i/self.N} % completed", end="\r", flush=True)
        elif algorithm == 2:
            # greedy
            for i in range(self.N):
                self.algo_samples.append(GreedyAlgo(region=region))
                print(f" {100 * i/self.N} % completed", end="\r", flush=True)
        elif algorithm == 3:
            # hillclimber
            start = time.time()
            n_runs = 0
            while time.time() - start < 3600:
                print(f"run: {n_runs}")
                self.algo_samples.append(Hillclimber(
                    region=region, reset_bound=reset_bound))
                n_runs += 1
        elif algorithm == 4:
            # alternative hillclimber
            start = time.time()
            n_runs = 0
            while time.time() - start < 3600:
                print(f"run: {n_runs}")
                self.algo_samples.append(Hillclimber_greedy(
                    region=region, reset_bound=reset_bound))
                n_runs += 1

    def max_K(self):
        """
        returns maximum K value and its object

        Returns
        -------
        dict
            key is the algo object and value is the max k value
        """
        k_max = -10000
        best_algo = None

        for algo in self.algo_samples:
            if algo.get_k() > k_max:
                k_max = algo.get_k()
                best_algo = algo

        return {best_algo: k_max}

    # function which returns mean median modus of dataset
    def stats(self):
        """
        returns several stats such as mean mode, standard deviation

        Returns
        -------
        dict
            stats as key and corresponding statistics value
        """
        dataset = []
        for algo in self.algo_samples:
            dataset.append(algo.get_k())

        return {"mean": statistics.mean(dataset), "mode": statistics.mode(dataset), "median": statistics.median(dataset),
                "stdev": statistics.stdev(dataset), "max": max(dataset), "min": min(dataset)}

    def histogram(self):
        """
        used for creating a histogram

        Returns
        -------
        list
            list of k values for histogram
        """
        dataset = []
        for algo in self.algo_samples:
            dataset.append(algo.get_k())
        return dataset
