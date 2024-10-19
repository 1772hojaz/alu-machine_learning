#!/usr/bin/env python3
"""
    a class MultiNormal that represents a Multivariate Normal distribution
"""

import numpy as np


class MultiNormal:
    def __init__(self, data):
        if type(data) != np.ndarray:
            raise TypeError("data must be a 2D numpy.ndarray")

        if len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = data.mean(axis=1).reshape(d, 1)
        m = data - self.mean
        self.cov = (m @ m.T) / (n - 1)
