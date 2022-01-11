class Station:
    """
    A class used to represent a Station

    ...

    Attributes
    ----------
    _city_name : str
        a string to keep track of which city it is in
    connections : dict
        dictionary of connections containing station object as key
        and time to travel as value
    _pos: tuple
        contains x,y coordinates of station
    Methods
    -------
    add_connection(station)
        adds connection between other station object
    get_city()
        returns city name
    get_position()
        returns position of station
    """

    def __init__(self, city_name, x_coord, y_coord):
        self._city_name = city_name
        self.connections = {}
        self._pos = (x_coord, y_coord)

    def add_connection(self, station, time):
        """
        add a connection between 2 stations

        Parameters
        ----------
        city : Station
            A station object
        time : int
            time to travel between 2 stations
        """
        self.connections[station] = time

    def get_city(self):
        """
        returns city name

        Returns
        -------
        str
            city_name string
        """
        return self.city_name

    def get_connections(self):
        return self.connections

    def get_position(self):
        return self._pos

    def has_connection(self, station):
        if station in self.connections.keys():
            return True
        else:
            return False

class Train:
    def __init__(self, starting_station):
        self.stations = [starting_station]

    def add_station(self, station):
        if self.stations[-1].has_connection(station):
            self.append(station)
        else:
            raise Exception('stations do not have a connection ')

