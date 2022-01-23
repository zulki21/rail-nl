from loader import load_stations
import random
from connection import Train

class GreedyAlgo:
    def __init__(self) -> None:
        self.stations = load_stations()
        self.trains = []
        self.used_connections = []
        self.all_connections = []