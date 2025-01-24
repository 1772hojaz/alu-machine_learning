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
        """
            cost fn
        """
        m = Y.shape[1]
        cost = -(1 / m) * np.sum(
                Y * np.log(A) + (1 - Y) * np.log(
                    1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """
            Evaluation of predictions
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)

        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        '''
            gradient descent
        '''
        m = Y.shape[1]
        dz = A - Y
        db = (1 / m) * np.sum(dz)
        dw = (1 / m) * np.matmul(X, dz.T)
        self.__W = self.__W - (alpha * dw.T)
        self.__b = self.__b - (alpha * db)


        return self.__W, self.__b
