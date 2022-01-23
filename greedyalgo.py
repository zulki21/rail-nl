from loader import load_stations
import random
from connection import Train

def get_k(trains, used_connections, minutes):

    return 10000 * (used_connections / 28) - (trains * 100 + minutes)

class GreedyAlgo:
    def __init__(self):
        self.stations = load_stations()
        self.trains = []
        self.used_connections = []

        while len(self.used_connections) != 28:

            # create starting station

            # append train

            # Chose which track is best for train (k value)

            # Let run for 120 min

            # repeat untill all tracks used


