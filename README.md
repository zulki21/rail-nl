# RailNL

RailNL consists of a problem which we as BetereNS try to solve.

## Getting Started

### Prerequisites

To run the following code some dependencies are needed these can be found in 'requirements.txt'. They can be installed using the following command:

```
pip install -r requirements.txt
```

### Structure

The structure of the files are as follows there are 4 main folders 'code', 'data', 'output_files' and 'plots'. 'code' contains all the code we have written. 'data' contains the data used in the research. 'output_files' contains raw csv files of the best samples we have found. 'plots' contains different graphs which show more insight into how different algorithms behave and compare to each other. In the tree below you can find some more information about every subfolder.

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

```bash
.
├── LICENSE
├── README.md
├── __init__.py
├── boxplot.py
├── code
│   ├── __init__.py
│   ├── algorithmRunner # Contains classes which run multiple samples of algorithm
│   ├── algorithms      # Contains different algorithm Classes
│   ├── mainCode        # Contains main object used e.g. Trains, Stations
│   └── visualization   # Code for visualization of output
├── copy2.py
├── data
│   ├── ConnectiesHolland.csv
│   ├── ConnectiesNationaal.csv
│   ├── StationsHolland.csv
│   └── StationsNationaal.csv
├── main.py
├── output_file
├── output_files
├── plots
│   ├── boxplots       # Boxplots of n samples from run
│   └── histograms     # Contains histograms of n samples for every algorithm
└── requirements.txt
```

### Usage

To get started right away using the

```
python main.py
```

```
python main.py 1 1 2 3
```

## Authors

- Zulkarneyn Catak
- Adrian Ruessink
- Robert Youseff

## Acknowledgments

- Marleen & Pamela
- minor programmeren van de UvA
- Random person on Stackoverflow
