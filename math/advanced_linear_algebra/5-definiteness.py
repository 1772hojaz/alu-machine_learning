#!/usr/bin/env python3
import numpy as np

"""
This function determines the definiteness of a given square matrix.
"""


def definiteness(matrix):
    """
    Determines the definiteness of a given square matrix.

    Args:
        matrix: A numpy.ndarray of shape (n, n)
        whose definiteness should be calculated.

    Raises:
        TypeError: If matrix is not a numpy.ndarray.

    Returns:
        A string indicating the definiteness of the matrix:
        "Positive definite", "Positive semi-definite",
        "Negative semi-definite", "Negative definite",
        "Indefinite", or None if the matrix is not valid.
    """

    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if not (matrix.ndim == 2 and (
            matrix.shape[0] == matrix.shape[1]) and (matrix.shape[0] > 0)):
        return None

    if not np.allclose(matrix, matrix.T):
        return None

    eig_vals = np.linalg.eigvalsh(matrix)

    if np.all(eig_vals > 0):
        return "Positive definite"
    elif np.all(eig_vals < 0):
        return "Negative definite"
    elif np.all(eig_vals == 0):
        return "Positive semi-definite" if np.all(
            eig_vals >= 0) else "Negative semi-definite"
    elif np.any(eig_vals > 0) and np.any(eig_vals < 0):
        return "Indefinite"

    return None
