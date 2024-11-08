import numpy as np


def create_grid(start, end, buffer=1, grid_size=0.1):
    x_min, y_min, x_max, y_max = (
        min(start.x, end.x) - buffer,
        min(start.y, end.y) - buffer,
        max(start.x, end.x) + buffer,
        max(start.y, end.y) + buffer,
    )
    grid_points = [
        (x, y)
        for x in np.arange(x_min, x_max, grid_size)
        for y in np.arange(y_min, y_max, grid_size)
    ]
    return grid_points


def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))
