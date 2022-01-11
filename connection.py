class Station:
    """
    A class used to represent a Station

    ...

    Attributes
    ----------
    city_name : str
        a string to keep track of which city it is in
    connections : list
        list of connections

    Methods
    -------
    add_connection(station)
        adds connection between other station object
    get_city()
        returns city name

    """

    def __init__(self, city_name):
        self.city_name = city_name
        self.connections = []

    def add_connection(self, station):
        """
        add a connection between 2 stations

        Parameters
        ----------
        city : Station
            A station object

        """
        self.connections.append(station)

    def get_city(self):
        """
        returns city name

        Returns
        -------
        str
            city_name string
        """
        return self.city_name


class Traject:
    def __init__(self):
        self.stations = []
