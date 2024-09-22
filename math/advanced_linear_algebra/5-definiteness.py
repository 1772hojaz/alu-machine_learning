#!/usr/bin/env python3
"""
this fn Determines the definiteness of a given square matrix.
"""

import numpy as np


def definiteness(matrix):

    """
        Determines the definiteness of a given square matrix.

        Args:
            matrix (numpy.ndarray): A square matrix of shape (n, n)
                for which the definiteness will be calculated.

        Raises:
            TypeError: If the input is not a numpy.ndarray.
            ValueError: If the matrix is not square or empty.

        Returns:
            str: A string indicating the definiteness:
                - "Positive definite"
                - "Negative definite"
                - "Negative semi-definite"
                - "Positive semi-definite"
                - "Indefinite"
                - None if the input matrix is invalid.
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

    if np.all(eig_vals > 0):
        return "Positive definite"
    elif np.all(eig_vals < 0):
        return "Negative definite"
    elif np.all(eig_vals <= 0):
        return "Negative semi-definite"
    elif np.all(eig_vals >= 0):
        return "Positive semi-definite"
    else:
        return "Indefinite"
