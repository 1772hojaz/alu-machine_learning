#!/usr/bin/env python3
import numpy as np
"""
this fn Determines the definiteness of a given square matrix.
"""


def definiteness(matrix):
    """
    Determines the definiteness of a given square matrix.

    Args:
        matrix: A numpy.ndarray of shape (n, n) whose
        definiteness should be calculated.

    Raises:
        TypeError: If matrix is not a numpy.ndarray.
    """

    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.shape[0] == 0:
        return None

    if any(not isinstance(row, np.ndarray)
           or len(row) != len(matrix) for row in matrix):
        return None

    if not np.allclose(matrix, matrix.T):
        return None

    eig_vals = np.linalg.eigvalsh(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    else:
        return "Indefinite"
