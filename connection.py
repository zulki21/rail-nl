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
        """
        returns connections station has

        Returns
        -------
        list
            list of stations that are connected
        """
        return self.connections

    def get_position(self):
        """
        returns x,y position of station as tuple

        Returns
        -------
        tuple
            tuple (x,y) coordinates
        """
        return self._pos

    def has_connection(self, station):
        """
        checks if station has connection with given station

        Parameters
        ----------
        station : Station
            station object
        """
        if station in self.connections.keys():
            return True
        else:
            return False

    def get_time(self, station):
        """
        returns time it takes between 2 stations

        Returns
        -------
        int
            time needed for travel
        """
        return self.connections[station]


class Train:
    """
    A class used to represent a Train route

    ...

    Attributes
    ----------
    route : list
        a list to keep track of stations train passes
    total_time : int
        total time the train will travel on the given route
    Methods
    -------
    add_station(station)
        adds station to route
    get_route()
        returns the list of stations train will pass
    get_time()
        returns total time trains journey will take
    """

    def __init__(self, starting_station):
        """
        Parameters
        ----------
        starting_station: Station object
            place where train will start his route
        """
        self.route = [starting_station]
        self.total_time = 0

    def add_station(self, station):
        """
        Adds station to the route and checking if station has connection

        Parameters
        ----------
        station: Station object
            station that will be added to route
        Raises
        ------
        Exception
            If there is no connection between the 2 stations
            an error will be raised
        """

        if self.route[-1].has_connection(station):
            self.total_time += self.get_time(station)
            self.append(station)
        else:
            raise Exception("last station does not have a connection ")

    def get_route(self):
        """
        returns the route of the train

        Returns
        -------
        list
            list of stations
        """
        return self.route

    def get_time(self):
        """
        returns the time it takes the train to finish the route

        Returns
        -------
        int
            total time travelled in minutes
        """
        return self.total_time
