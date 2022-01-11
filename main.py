from loader import load_stations
from connection import Train, Station
import random

if __name__ == "__main__":
    stations = load_stations()
    starting_station = random.choice(list(stations.values()))

    train_1 = Train(starting_station)
    next_station = starting_station
    for i in range(4):
        next_station = random.choice(list(next_station.get_connections().keys()))
        
        train_1.add_station(next_station)

    print(train_1.get_time_route())
    print(train_1.get_route())

    for train in train_1.get_route():
        print(train._city_name)