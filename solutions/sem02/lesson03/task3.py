import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) >= 3:
        maxy = (ordinates[1:-1] > ordinates[2:]) & (ordinates[1:-1] > ordinates[:-2])
        miny = (ordinates[1:-1] < ordinates[2:]) & (ordinates[1:-1] < ordinates[:-2])
        idnices = np.arange(1, len(ordinates) - 1)
        return (idnices[miny], idnices[maxy])
    raise ValueError
