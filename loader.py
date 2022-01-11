from connection import Station
from connection import Train

import csv

def load_stations():

    stations = {}

    with open("StationsHolland.csv") as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:
            
            stations[row[0]] = Station(row[0], row[1], row[2])

        
load_stations()