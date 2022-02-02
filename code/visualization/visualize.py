import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import matplotlib.pyplot as plt
from tabulate import tabulate


# this function returns all the important information which is stored inside the routes and connections
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


# this function returns the important information from the stations
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


# this function plots the traces of the trains
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


# no matter which algorithm you run, this function will visualize a histogram for the selected options
def visualize_histogram(algos, output_file_hist, title, label):
    plt.figure(figsize=(6, 5))

    for algo_runner in algos:
        # Plot histogram
        plt.hist(algo_runner.histogram(), bins='auto')

    # Labels for the histogram
    plt.xlabel("K-values")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.legend(label)

    plt.savefig(output_file_hist)


# no matter which algorithm you run, this function will visualize a tabel for the selected options
# this tabel will be printed in the terminal
def create_tabel(algos):
    for algo_runner in algos:
        content = algo_runner.stats().items()
        print(tabulate(content, tablefmt="github"))


# no matter which algorithm you run, this function will visualize a boxplot for the selected options
def visualize_boxplot(algos, output_file_box, label):
    plt.figure(figsize=(6, 5))
    colors = ['blue', 'green', 'yellow', 'black', 'brown', 'purple']

    # extracts the k-values and saves it
    all_k_values = []
    for i, algo_runner in enumerate(algos):
        box_data = algo_runner.algo_samples
        k_values = []

        # Extracts the k_values for each run
        for j in range(len(box_data)):
            k = box_data[j].get_k()
            k_values.append(k)

        all_k_values.append(k_values)

    # plots the boxplot
    box = plt.boxplot(all_k_values, patch_artist=True)

    # sets the colors for the different boxplots
    for i, patch in enumerate(box['boxes']):
        patch.set_facecolor(colors[i])

    # styling the labels and saving the graph
    if len(all_k_values) > 1:
        plt.xticks(list(range(1, len(all_k_values) + 1)), label[:-1])
    else:
        plt.xticks([1], label)
    plt.ylabel('k-values')
    plt.savefig(output_file_box, format="png")
