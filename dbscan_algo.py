import geopandas as gpd
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from shapely.geometry import Point
import folium

outbreaks = gpd.read_file("export.geojson")
districts = gpd.read_file("gadm41_IND_2.json")

outbreaks = outbreaks.to_crs(epsg=4326)
outbreak_coords = outbreaks.geometry.apply(lambda p: (p.y, p.x)).tolist()

coords_df = pd.DataFrame(outbreak_coords, columns=["lat", "lon"])
db = DBSCAN(eps=0.002, min_samples=10, metric='haversine').fit(np.radians(coords_df))
outbreaks["cluster"] = db.labels_

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

n_noise = (outbreaks["cluster"] == -1).sum()
print(f"Number of noise points: {n_noise}")

m = folium.Map(location=[coords_df["lat"].mean(), coords_df["lon"].mean()], zoom_start=5)
folium.GeoJson(districts, name="Districts").add_to(m)

for idx, (i, row) in enumerate(outbreaks.iterrows()):
    cluster_id = row["cluster"]
    lat, lon = row.geometry.y, row.geometry.x

    if cluster_id == -1:
        # Noise: blue marker
        folium.Marker(
            location=[lat, lon],
            icon=folium.Icon(color='blue', icon='exclamation', prefix='fa'),
            popup="Noise Point"
        ).add_to(m)
    elif core_samples_mask[idx]:
        folium.CircleMarker(
            location=[lat, lon],
            radius=6,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.9,
            popup=f"Core Point (Cluster {cluster_id})"
        ).add_to(m)
    else:
        folium.CircleMarker(
            location=[lat, lon],
            radius=5,
            color='yellow',
            fill=True,
            fill_color='yellow',
            fill_opacity=0.7,
            popup=f"Border Point (Cluster {cluster_id})"
        ).add_to(m)

def compute_centroid(group: gpd.GeoDataFrame) -> pd.Series:
    return pd.Series({
        'lat': group.geometry.y.mean(),
        'lon': group.geometry.x.mean()
    })

valid_clusters = outbreaks[outbreaks["cluster"] != -1].groupby("cluster")
deployment_locations = valid_clusters.apply(compute_centroid, include_groups=False)

for cluster_id, row in deployment_locations.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        icon=folium.Icon(color='darkgreen', icon='plus-square', prefix='fa'),
        popup=f"Health Unit for Cluster {cluster_id}"
    ).add_to(m)

m.save("dbscan_clusters_map.html")
print("Map saved as dbscan_clusters_map.html")