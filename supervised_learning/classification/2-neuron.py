#!/usr/bin/env python3
"""
    Neuron that defines a single performing binary classification
"""


import numpy as np


class Neuron:
    """
    Repalced public attributes to private attributes
    """
    def __init__(self, nx):

        if type(nx) is not int:
            raise TypeError("nx must be a integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A

    def forward_prop(self, X):
        x = np.array(X)
        nx = self.nx
        m = X.size
        x = x.reshape(nx, m)

