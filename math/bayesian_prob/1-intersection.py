#!/usr/bin/env python3
"""
    a function that calculates  the intersection of
    obtaing this data with the various hypothetical
    probabilities
"""
import numpy as np


def intersection(x, n, P, Pr):
    """
        Calculates the intersection of obtaining the data with
        the various hypothetical probabilities.

        Parameters:
        x (int): The number of patients that develop severe side effects.
        n (int): The total number of patients observed.
        P (numpy.ndarray): A 1D numpy.ndarray containing the various
        hypothetical probabilities
                        of developing severe side effects.
        Pr (numpy.ndarray): A 1D numpy.ndarray containing
        the prior beliefs of P.

        Returns:
        numpy.ndarray: A 1D numpy.ndarray containing the
        intersection of obtaining x and n
                    with each probability in P.

        Raises:
        ValueError: If n is not a positive integer.
                    If x is not an integer greater than or equal to 0.
                    If x is greater than n.
                    If any value in P or Pr is not in the range [0, 1].
                    If Pr does not sum to 1.
        TypeError: If P is not a 1D numpy.ndarray.
                If Pr is not a numpy.ndarray with the same shape as P.
    """

    if not isinstance(n, int) or (n <= 0):
        raise ValueError('n must be a positive integer')

    if not isinstance(x, int) or (x < 0):
        err = 'x must be an integer that is greater than or equal to 0'
        raise ValueError(err)

    if x > n:
        raise ValueError('x cannot be greater than n')

    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError('P must be a 1D numpy.ndarray')

    if np.any(P > 1) or np.any(P < 0):
        raise ValueError('All values in P must be in the range [0, 1]')

    if not isinstance(Pr, np.ndarray) or (P.shape != Pr.shape):
        err = 'Pr must be a numpy.ndarray with the same shape as P'
        raise TypeError(err)

    if np.any(Pr > 1) or np.any(Pr < 0):
        raise ValueError('All values in Pr must be in the range [0, 1]')

    E = np.sum(Pr)
    if not np.isclose(E, 1):
        raise ValueError('Pr must sum to 1')
    Fact1 = (np.math.factorial(n))
    Fact2 = (np.math.factorial(x) * np.math.factorial(n - x))
    factorial = Fact1 / Fact2
    factorial *= (np.power(P, x)) * (np.power((1 - P), (n - x)))
    return factorial * Pr
