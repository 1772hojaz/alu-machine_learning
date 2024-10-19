#!/usr/bin/env python3
import numpy as np

def mean_cov(x):
    if not isinstance(x, np.ndarray) or x.ndim !=2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n,d = x.shape
    if n < 2 :
        raise ValueError("X must contain multiple data points")
    mean = []
    mean = np.mean(x, axis=0)
    cov = np.cov(x, rowvar=False)
    return mean, cov
