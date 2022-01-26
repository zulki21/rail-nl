from connection import Station

import csv


def load_stations():

    stations = {}

    # Adds all stations and location to class
    with open("StationsNationaal.csv") as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:

            stations[row[0]] = Station(row[0], row[1], row[2])

    # Adds all connections to the stations
    with open("ConnectiesNationaal.csv") as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:

            station1 = stations[row[0]]
            station2 = stations[row[1]]

            station1.add_connection(station2, row[2])
            station2.add_connection(station1, row[2])

    return stations
