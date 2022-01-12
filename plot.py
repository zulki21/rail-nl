import pandas as pd
import matplotlib.pyplot as plt
import argparse
import plotly.express as px
# import plotly.graph_objects as go
import geopandas as gpd
# import folium
# import warnings
# from mpl_toolkits.basemap import Basemap


# def main(input_file, output_file):

df = pd.read_csv('StationsHolland.csv')
# print(df.x)

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

fig = px.scatter_mapbox(df, lat=df.x, lon=df.y, hover_name="station", hover_data=["x", "y"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

# file_path = 'Provinciegrenzen/B1_Provinciegrenzen_van_NederlandPolygon.shp'
# gdf_prov = gpd.read_file(file_path)

# my_map = Basemap(projection='merc', resolution='h', area_thresh=30,
#                  llcrnrlon=map_boundaries.left,
#                  llcrnrlat=map_boundaries.bottom,
#                  urcrnrlon=map_boundaries.right,
#                  urcrnrlat=map_boundaries.top)

# # fill the map
# my_map.drawcoastlines()
# my_map.drawcountries()
# my_map.fillcontinents(color='moccasin')

# print(gdf_prov)
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# fig, ax = plt.subplots(figsize=(8, 8))

# gdf_prov.plot(ax=ax, facecolor='none', edgecolor='gray')

# ax.scatter(list(map(lambda x: x * 10000, df.y)),
#            list(map(lambda x: x * 10000, df.x)))  # TODO: dit gebruiken

# print(gdf_prov.crs)

# print(df.head())

# print(boundingBox[3])

# fig, ax = plt.subplots(figsize=(10, 5))

# fig = px.scatter_geo(df.x, df.y)

# plt.show()

# fig.savefig(output_file, format='png')
# fig.write_image(output_file)

# fig = go.Figure(go.Scattermapbox(
#     lat=[df.x], lon=[df.y], mode='markers'))

# fig.show()

# fig.show()
# print(fig)

# go.savefig(output_file, format='png')
# fig.write_image(output_file)

# fig = px.scatter_geo(df, lat=df.x, lon=df.y)
# fig.update_layout(title='World map', title_x=0.5)
# fig.show()

# nld_lat = 52.2130
# nld_lon = 5.2794

# nld_coordinates = (nld_lat, nld_lon)

# # Maak kaart van Nederland
# map_nld = folium.Map(location=nld_coordinates,
#                      tiles='cartodbpositron', zoom_start=7, control_scale=True)

# Toon resultaat
# print(map_nld)
# plt.savefig(output_file, format='png')


# if __name__ == "__main__":
#     # Set-up parsing command line arguments
#     parser = argparse.ArgumentParser(description="plots a graph from the data")

#     # Adding arguments
#     parser.add_argument("input", help="location of datafile")
#     parser.add_argument("output", help="location of output file")

#     # Read arguments from command line
#     args = parser.parse_args()

#     # Run main with provide arguments
#     main(args.input, args.output)
