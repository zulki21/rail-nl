import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
from loader import load_stations
from connection import Train


df = pd.read_csv('StationsHolland.csv')
print(df)

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

fig = px.scatter_mapbox(lat=df.x, lon=df.y, hover_name=df.station,
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# fig.add_trace(go.Scattermapbox(
#     mode="lines",
#     lon=df.y,
#     lat=df.x,
#     marker={'size': 10}))

# fig.show()
