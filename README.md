# RailNL

RailNL consists of a problem which we as BetereNS try to solve.

## Getting Started

### Prerequisites

To run the following code some dependencies are needed these can be found in 'requirements.txt'. They can be installed using the following command:

```
pip install -r requirements.txt
```

### Structure

The structure of the files are as follows

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
