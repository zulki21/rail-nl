import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import matplotlib.pyplot as plt
from code.algorithmRunner.algorunner import *
from code.algorithmRunner.greedyrunner import GreedyRunner
from tabulate import tabulate
import numpy as np


def get_route(trains):
    lats = []
    lons = []
    positions = []
    b = []
    traces_lat = []
    traces_lon = []
    station_traces = []

    for train in trains:
        station_list = train.get_route()
        lat = []
        lon = []
        stations = []
        for station in station_list:
            b.append(station.get_name())
            stations.append(station.get_name())
            positions.append(station.get_position())
            lat.append(float(station.get_position()[0]))
            lon.append(float(station.get_position()[1]))
            lats.append(float(station.get_position()[0]))
            lons.append(float(station.get_position()[1]))
        traces_lat.append(lat)
        traces_lon.append(lon)
        station_traces.append(stations)

    return lat, lon, lats, lons, positions, b, traces_lat, traces_lon


def get_all_stations(stations):
    station_names = []
    station_positions = []
    station_lats = []
    station_lons = []

    for station_name, station_obj in stations.items():
        station_names.append(station_name)
        station_positions.append(station_obj.get_position())
        station_lats.append(float(station_obj.get_position()[0]))
        station_lons.append(float(station_obj.get_position()[1]))
    return station_names, station_positions, station_lats, station_lons


def visualize_all_routes(trains, stations):
    lat, lon, lats, lons, positions, b, traces_lat, traces_lon = get_route(
        trains)
    station_names, station_positions, station_lats, station_lons = get_all_stations(
        stations)

    gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

    fig = px.scatter_mapbox(station_positions, lat=station_lats,
                            lon=station_lons, hover_name=station_names)
    px.scatter_mapbox(positions, lat=lats, lon=lons, hover_name=b,
                      color_discrete_sequence=["fuchsia"], height=300)
    for i in range(len(trains)):

        fig = fig.add_trace(go.Scattermapbox(
            mode="lines",
            lon=traces_lon[i],
            lat=traces_lat[i],
            marker={'size': 5},
            hoverinfo='skip'
        ))

    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0,
                              "b": 0}, width=1500, height=700, mapbox={
        'center': {'lon': 4.900277615, 'lat': 52.37888718}})

    fig.show()


def randomHist():
    plt.figure(figsize=(5, 4))

    RunsRandom = AlgoRunner(1000)
    # Plot histogram
    plt.hist(RunsRandom.histogram_random(), bins='auto')

    # Labels for the histogram
    plt.xlabel("K-values")
    plt.ylabel("Frequency")
    plt.title('Random Algorithm')
    # plt.legend(['Greedy', 'Random'])

    # Save histogram as a png
    plt.savefig('plots/histogram_Random.png')


def greedyHist():
    plt.figure(figsize=(5, 4))

    RunsGreedy = GreedyRunner(1000)
    # Plot histogram

    plt.hist(RunsGreedy.histogram_greedy(), bins='auto')

    # Labels for the histogram
    plt.xlabel("K-values")
    plt.ylabel("Frequency")
    plt.title('Greedy Algorithm')

    # Save histogram as a png
    plt.savefig('plots/Histogram-Greedy.png')


def createTabelRandom():

    RandomTabelRuns = AlgoRunner(1000)
    content = RandomTabelRuns.stats().items()
    print(content)
    print(tabulate(content, tablefmt="github"))


def createTabelGreedy():
    GreedyTabelRuns = GreedyRunner(1000)
    content = GreedyTabelRuns.stats().items()
    print(content)
    print(tabulate(content, tablefmt="github"))


def visualize_boxplot_Random():
    plt.figure(figsize=(6, 5))
    # Runs the random algorithm
    RandomRuns = AlgoRunner(1000)

    # Stores all the seperate runs
    box_data = RandomRuns.algo_samples

    k_values = []

    # Extracts the k_values for each run
    for i in range(len(box_data)):

        k = box_data[i].get_k()
        print(k)
        k_values.append(k)

    # Saves the boxplot (More plots will be added with more algorithms)
    plt.boxplot(k_values, patch_artist=True, labels=['random'])
    plt.ylabel('k-values')
    plt.savefig("plots/boxplot_Random.png", format="png")


def visualize_boxplot_Greedy():
    plt.figure(figsize=(6, 5))
    # Runs the greedy algorithm
    GreedyRuns = GreedyRunner(1000)

    # Stores all the seperate runs
    box_data = GreedyRuns.algo_samples

    k_values = []

    # Extracts the k_values for each run
    for i in range(len(box_data)):

        k = box_data[i].final_k()
        print(k)
        k_values.append(k)

    # Saves the boxplot (More plots will be added with more algorithms)
    plt.boxplot(k_values, patch_artist=True, labels=['greedy'])
    plt.ylabel('k-values')
    plt.savefig("plots/boxplot_Greedy.png", format="png")
