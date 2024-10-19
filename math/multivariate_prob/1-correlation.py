#!/usr/bin/env python3
""" This function calculates a correlation matrix """

import numpy as np


def correlation(C):
    """
    C: numpy.ndarray of shape (d, d)
        Contains the covariance matrix, where:
        d: number of dimensions

    Raises:
        TypeError: if C is not a numpy.ndarray
        ValueError: if C does not have shape (d, d)

    Returns:
        numpy.ndarray of shape (d, d)
            The correlation matrix.
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2:
        raise ValueError("C must be a 2D square matrix")

    cor = np.corrcoef(C).reshape(2, 2)
    return cor

