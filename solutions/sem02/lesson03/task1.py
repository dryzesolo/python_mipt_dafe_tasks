import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape == rhs.shape:
        return lhs + rhs
    raise ShapeMismatchError


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return 3 * abscissa ** 2 + 2 * abscissa + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError
    diffs = (lhs[:, np.newaxis, :] - rhs[np.newaxis, :]) ** 2
    return np.sqrt(np.sum(diffs, axis=2))