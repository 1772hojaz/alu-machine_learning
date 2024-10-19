#!/usr/bin/env python3
import numpy as np
"""Function that calculates the mean and covariance of a data set"""


def mean_cov(x):
    """this function calculates mean and covarience"""
    if not isinstance(x, np.ndarray) or x.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n, d = x.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.mean(x, axis=0).reshape(1, d)
    centered = x - mean

    cov = (centered.T @ centered) / (n-1)
    return mean, cov
