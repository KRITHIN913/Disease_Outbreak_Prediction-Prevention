import geopandas as gpd
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from shapely.geometry import Point
import folium


outbreaks = gpd.read_file("export.geojson")
districts = gpd.read_file("gadm41_IND_2.json")

outbreaks = outbreaks.to_crs(epsg=4326)
outbreak_coords = outbreaks.geometry.apply(lambda p: (p.y, p.x)).tolist()

coords_df = pd.DataFrame(outbreak_coords, columns=["lat", "lon"])
agglo = AgglomerativeClustering(n_clusters=5, metric='euclidean', linkage='ward')
outbreaks["cluster"] = agglo.fit_predict(coords_df)

m = folium.Map(location=[coords_df["lat"].mean(), coords_df["lon"].mean()], zoom_start=5)
folium.GeoJson(districts, name="Districts").add_to(m)

colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'cadetblue', 'darkred', 'darkblue', 'darkgreen']
for i, row in outbreaks.iterrows():
    cluster_id = row["cluster"]
    lat, lon = row.geometry.y, row.geometry.x
    color = colors[cluster_id % len(colors)]

    folium.CircleMarker(
        location=[lat, lon],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.8,
        popup=f"Cluster {cluster_id}"
    ).add_to(m)

def compute_centroid(group):
    return pd.Series({
        'lat': group.geometry.y.mean(),
        'lon': group.geometry.x.mean()
    })

valid_clusters = outbreaks.groupby("cluster")
deployment_locations = valid_clusters.apply(compute_centroid)

for cluster_id, row in deployment_locations.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        icon=folium.Icon(color='darkgreen', icon='plus-square', prefix='fa'),
        popup=f"Health Unit for Cluster {cluster_id}"
    ).add_to(m)

m.save("Agglomerative _clusters_map.html")
print("Map saved as Agglomerative _clusters_map.html")