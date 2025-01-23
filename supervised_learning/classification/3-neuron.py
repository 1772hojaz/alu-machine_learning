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
        self.nx = nx
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
        """
            so Basically a neuron has Y =mX + b and
            a nonlinearisation function.in this case a
            sigmoid function.
        """

        w = self.__W
        b = self.__b

        z = 1/(1 + np.exp(-1 * (np.dot(w, X) + b)))
        self.__A = z

        return self.__A

    def cost(self, Y, A):

        m = Y.shape[1]
        cost = -(1 / m) * np.sum(
                Y * np.log(A) + (1.0000001 - Y) * np.log(
                    1.0000001 - A))
        return cost
