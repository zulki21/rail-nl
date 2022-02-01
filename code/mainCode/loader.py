from code.mainCode.connection import Station

import csv


def load_stations(region):
    if region == 1:
        load_stations = "data/StationsHolland.csv"
        load_connections = "data/ConnectiesHolland.csv"

    elif region == 2:
        load_stations = "data/StationsNationaal.csv"
        load_connections = "data/ConnectiesNationaal.csv"
    else:
        raise Exception("Argument not valid")

    stations = {}

    # Adds all stations and location to class
    with open(load_stations) as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:

            stations[row[0]] = Station(row[0], row[1], row[2])

    # Adds all connections to the stations
    with open(load_connections) as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:

            station1 = stations[row[0]]
            station2 = stations[row[1]]

            station1.add_connection(station2, row[2])
            station2.add_connection(station1, row[2])

    return stations
