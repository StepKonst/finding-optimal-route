import networkx as nx
import numpy as np
from shapely.geometry import Point


def build_graph(grid_points, polygons, start, end, grid_size) -> nx.Graph:
    G = nx.Graph()

    for point in grid_points:
        p = Point(point)
        if not any(p.within(poly) for poly in polygons):
            G.add_node((p.x, p.y))

    G.add_node((start.x, start.y))
    G.add_node((end.x, end.y))

    nodes = list(G.nodes)
    for i, node1 in enumerate(nodes):
        for j in range(i + 1, len(nodes)):
            node2 = nodes[j]
            distance = np.linalg.norm(np.array(node1) - np.array(node2))
            if distance < grid_size * 1.5:
                G.add_edge(node1, node2, weight=distance)

    return G


def find_path(graph, start, end) -> list:
    try:
        path = nx.astar_path(
            graph,
            (start.x, start.y),
            (end.x, end.y),
            heuristic=lambda a, b: np.linalg.norm(np.array(a) - np.array(b)),
        )
        return path
    except nx.NetworkXNoPath:
        print("Путь не найден между указанными точками.")
        return None
