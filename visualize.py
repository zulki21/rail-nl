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


def get_all_routes(trains):
    lat, lon, lats, lons, positions, b, traces_lat, traces_lon = get_route(
        trains)
    gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

    fig = px.scatter_mapbox(positions, lat=lats, lon=lons, hover_name=b,
                            color_discrete_sequence=["fuchsia"], zoom=3, height=300)
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
