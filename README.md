# RailNL

RailNL consisted of a problem which we as BetereNS tried to solve.

## Getting Started

The most important goal for this case was to design an optimized route for intercitytrains.
This case consisted of two parts.

### Part one (North- and South-Holland)

In part one the assignment was to optimize the quality of the routes of north- and south-Holland by adhering to a number of restrictions. These restrictions were:

- a maximum number of 7 routes
- a timeframe of 2 hours
- all connections must be ridden

To improve the quality of the routes we used the following formula:

```
K = p*10000 - (T*100 + Min)
K = quality of the routes
p = fraction of the ridden connections (between 0 and 1)
T = number of routes
Min = number of minutes
```

### Part two The Netherlands

The goal of the second part of the case remained the same. The same formula was used to optimize the K-value of the routes.The restrictions in this part were different as all stations were used as opposed to the routes in only two provinces:

- a maximum number of 20 routes
- a timeframe of 3 hours
- all connections must be ridden

## Used Algorithms

In this case, we used 4 different algorithms. The goal for using these algorithms was to optimize the k-value of the routes. The higher the k-value, the better and the more optimized the routes were.

### Random algorithm

The random algoritm chooses a random number of trains between 1,7 and 1,20 given the different maps. All of these trains will have a random starting station from where they will start their random path up untill they reach the time limit.

### Greedy algorithm

The greedy algorithm choses the route of the train based on the k value. It starts off by chosing a random starting station which has unused connections. Then when the train needs to make a choice of which connection to take, it first calculates the effect each one has on the k value. It then uses the connection which gives the highest k value.

### Hillclimber algorithm

The hillclimber algorithm will start with a random state space created by the random algorithm then it will remove 3 trains and start adding new random trains. After comparing the k-values the algorithm will decide whether or not to use the new trains of revert back to the original ones. The user has to specify a bound on how many times the algorithm is allowed to get a lower k-value then the best one. After this bound is hit the algorithm will stop. Our research has found that the k-value converges around 1000 iterations.

### Hillclimber-greedy algorithm

This algorithm is a variation of the standard hillclimber algorithm it is very similar to the steepest ascent Hillclimbing algorithm. The main difference between the two algorithms is that the small change which is made is not random but decided using the greedy algorithm. This algorithm allows for more local optimization of the problem.

### Output examples

Three examples of generated output could be a plot, a graph, a tabel.
These examples are shown below:
<img src="data/visualisatie random algorithm.png" width="20%" height="50%"/>
<img src="data/Histogram.png" width="30%" height="30%"/>
<img src="data/tabel greedy.png" width="30%" height="30%"/>

### Prerequisites

To run the following code some dependencies are needed. These can be found in `requirements.txt`. They can be installed using the following command:

```
pip install -r requirements.txt
```

### Structure

The structure of the files are as follows, there are 4 main folders `code`, `data`, `output_files` and `plots`. `code` contains all written codes. `data` contains the data used in the research. `output_files` contains raw csv files of the best samples we have found. `plots` contains different graphs which provides insight into how different algorithms behave and compare to each other. In the tree below you can find some more information about the subfolders. Furthermore the root directory contains `main.py` which is necessary to run the function according to the users needs.

```bash
.
.
├── code
│   ├── algorithmRunner # Contains classes which run multiple samples of algorithm
│   ├── algorithms      # Contains different algorithm Classes
│   ├── mainCode        # Contains main object used e.g. Trains, Stations
│   └── visualization   # Code for visualization of output
├── data
├── output_files        # Raw csv files with output of best sample from run
└── plots
    ├── boxplots        # Boxplots of n samples from run
    └── histograms      # Contains histograms of n samples for every algorithm
```

### Usage

To get started right away, run the following commands

<!-- <img src="/data/video.gif" width="100%" height="50%"/> -->
<img src="/data/video_verbeterd.gif" width="100%" height="50%"/>

```
python main.py
```

```
python main.py 1 1 2 3
```

This command will provide you with some tabels, plots and graphs depending on the options that you have specified.

## Authors

- Zulkarneyn Catak
- Adrian Ruessink
- Robert Youssef

## Acknowledgments

- Marleen & Pamela
- minor programmeren van de UvA
- Random person on Stackoverflow

## Easter egg

```
sudo apt install sl
```

try installing this command and then running 'sl' in the terminal ☺
