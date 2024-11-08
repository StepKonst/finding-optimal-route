import geopandas as gpd
from shapely.geometry import Point, Polygon

from pathfinding.graph_utils import create_grid
from pathfinding.pathfinding import build_graph, find_path
from pathfinding.visualization import visualize_route


def main() -> None:

    data = gpd.read_file("data/data.geojson")
    start = Point(data["geometry"][0])
    end = Point(data["geometry"][1])
    polygons = [Polygon(data["geometry"][i]) for i in range(2, len(data["geometry"]))]

    grid_points = create_grid(start, end)
    G = build_graph(grid_points, polygons, start, end, grid_size=0.1)

    path = find_path(G, start, end)

    visualize_route(path, start, end, polygons)


if __name__ == "__main__":
    main()
