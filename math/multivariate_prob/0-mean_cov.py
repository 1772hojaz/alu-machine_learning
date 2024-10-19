#!/usr/bin/env python3
import numpy as np
"""
This function calculates the mean and covarience od a data set

"""


def mean_cov(x):
    """
    x is a numpy,ndarray of shape (n, d) containg the data set
    n is the number of data points
    d is the number of dimenissions in each data point
    the mean is a numpy.ndarray of shape (1, d)

    """
    if not isinstance(x, np.ndarray) or x.ndim !=2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n,d = x.shape
    if n < 2 :
        raise ValueError("X must contain multiple data points")

    mean = np.mean(x, axis=0).reshape(1, d)
    centered = x - mean

    cov = (centered.T @ centered) / (n-1)
    return mean, cov
