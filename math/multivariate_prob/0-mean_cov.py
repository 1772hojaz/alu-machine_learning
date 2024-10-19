#!/usr/bin/env python3
import numpy as np


def mean_cov(x):
    """
        x: numpy.ndarray of shape (n, d)
            Contains the dataset, where:
            n: number of data points
            d: number of dimensions in each data point

        mean: numpy.ndarray of shape (1, d)
            The mean of the dataset.
    """
    if not isinstance(x, np.ndarray) or x.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n, d = x.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.mean(x, axis=0).reshape(1, d)
    centered = x - mean

    cov = (centered.T @ centered) / (n-1)
    return mean, cov
