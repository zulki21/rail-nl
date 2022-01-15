from loader import load_stations
from connection import Train
import random
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import pandas as pd
from pandas.core.frame import DataFrame


def unique_connection_train(train):
    """
    finds all unique connections of this train

    Parameters
    ----------
    train: train object
        will look at route of train
    Returns
    ------
    list of lists
        contains unique combination of every connection in route
    """

    pairs = []
    i = 0
    route = train.get_route()

    for i in range((len(route) - 1)):
        pairs.append([route[i].get_name(), route[i + 1].get_name()])

    unique_pairs = []
    for pair in pairs:
        unique_pairs.append(sorted(pair))

    b_set = set(tuple(x) for x in unique_pairs)
    b = [list(x) for x in b_set]

    return b


def unique_total_connections(list_of_trains):
    """
    finds all unique connections of all trains

    Parameters
    ----------
    train: train object
        will look at route of train
    Returns
    ------
    list of lists
        contains unique combination of every connection in route
    """
    unique_pairs = []

    combis = []
    for train in list_of_trains:
        abc = unique_connection_train(train)
        combis.extend(abc)

    for pair in combis:
        unique_pairs.append(sorted(pair))

    b_set = set(tuple(x) for x in unique_pairs)
    b = [list(x) for x in b_set]

    return len(b)


def total_time_trains(trains):
    min = 0
    for train in trains:
        min += train.get_time_route()

    return min


if __name__ == "__main__":
    stations = load_stations()

    trains = []

    # adding routes to the trains randomly
    for i in range(5):
        starting_station = random.choice(list(stations.values()))

        trains.append(Train(starting_station))

    for train in trains:
        current_station = train.get_route()[0]
        for i in range(5):
            connections = list(current_station.get_connections().keys())
            next_station = random.choice(connections)
            if train.get_time_route() + current_station.get_time(next_station) < 120:

                train.add_station(next_station)
                current_station = next_station

    a = unique_total_connections(trains)

    min = total_time_trains(trains)

    K = 10000 * (a / len(stations)) - (len(trains) * 100 - min)

    for train in trains:
        station_list = train.get_route()
        a = []
        position = []
        lat = []
        lon = []
        for station in station_list:
            a.append(station.get_name())
            position.append(station.get_position())
            lat.append(station.get_position()[0])
            lon.append(station.get_position()[1])

        lat = list(map(float, lat))
        lon = list(map(float, lon))
        # print(lat)
        geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

        fig = px.scatter_mapbox(position, lat=lat, lon=lon, hover_name=a,
                                color_discrete_sequence=["fuchsia"], zoom=3, height=300)
        fig.add_trace(go.Scattermapbox(
            mode="lines",
            lon=lon,
            lat=lat,
            marker={'size': 5},
            showlegend=False))
        fig.update_layout(mapbox_style="carto-positron")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        fig.show()
    # print(lon)
    # print(position)
    print(a)
    print("------------")
    print(K)

    # for coordinate in position:
    #     print(coordinate)

    # pd.to_numeric(df_pos)
    # print(lat)

    # geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

    # fig = px.scatter_mapbox(position, lat=lat, lon=lon, hover_name=a,
    #                         color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    # fig.add_trace(go.Scattermapbox(
    #     mode="lines",
    #     lon=lon,
    #     lat=lat,
    #     marker={'size': 5},
    #     showlegend=False))
    # fig.update_layout(mapbox_style="carto-positron")
    # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    # fig.show()

    # df_pos = pd.DataFrame(position, columns=list('xy'))
