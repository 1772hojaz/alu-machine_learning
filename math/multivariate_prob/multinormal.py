#!/usr/bin/env python3
"""
    a class MultiNormal that represents a Multivariate Normal distribution
"""

import numpy as np


class MultiNormal:
    """
        Multi-variable Normal distribution
    """
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

    def pdf(self, x):
        """
            Calculates the PDF at a data point.

            Args:
                x (numpy.ndarray): The data point of shape (d, 1).

            Raises:
                TypeError: If x is not a numpy.ndarray.
                ValueError: If x does not have shape (d, 1).

            Returns:
                float: The value of the PDF at x.
        """
        d = self.cov.shape[0]

        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        
        if len(x.shape) != 2 or x.shape[1] != 1 or x.shape[0] != d:
            raise ValueError("x must have the shape ({}, 1)".format(d))
        
        

        det = np.linalg.det(self.cov)

        inverse = np.linalg.inv(self.cov)

        fst = 1 / ((2 * np.pi) ** (d / 2) * np.sqrt(det))

        sec = np.dot((x - self.mean).T, inverse)

        thrd = np.dot(sec, (x - self.mean) / -2)

        pdf = fst * np.exp(thrd)

        return pdf[0][0]
