class Station:
    """
    A class used to represent a Station

    ...

    Attributes
    ----------
    city_name : str
        a string to keep track of which city it is in
    connections : dict
        dictionary of connections containing station object as key and time to travel as value

    Methods
    -------
    add_connection(station)
        adds connection between other station object
    get_city()
        returns city name

    """

    def __init__(self, city_name):
        self.city_name = city_name
        self.connections = {}

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


class Traject:
    def __init__(self):
        self.stations = []
