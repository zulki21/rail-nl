import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd


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
