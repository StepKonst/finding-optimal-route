import folium
import geopandas as gpd
from shapely.geometry import LineString


def visualize_route(path, start, end, polygons) -> None:
    if not path:
        return

    gdf = gpd.GeoDataFrame(geometry=[LineString(path)], crs="EPSG:4326")
    gdf.to_file("data/new-route.geojson", driver="GeoJSON")

    m = folium.Map(
        location=[(start.y + end.y) / 2, (start.x + end.x) / 2], zoom_start=12
    )

    folium.Marker(
        [start.y, start.x], popup="Start", icon=folium.Icon(color="green")
    ).add_to(m)
    folium.Marker([end.y, end.x], popup="End", icon=folium.Icon(color="red")).add_to(m)

    for poly in polygons:
        folium.GeoJson(
            poly,
            style_function=lambda x: {
                "fillColor": "orange",
                "color": "orange",
                "weight": 2,
                "fillOpacity": 0.4,
            },
        ).add_to(m)

    folium.PolyLine(
        [(lat, lon) for lon, lat in path],
        color="blue",
        weight=3,
        opacity=0.7,
        tooltip="Route",
    ).add_to(m)

    m.save("map/map.html")
