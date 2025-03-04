#!/usr/bin/env python3
"""
calculates the likelihood of obtaining this
data given various hypothetical probabilities
of developing severe side effects
"""
import numpy as np


def likelihood(x, n, P):
    """
    Calculates the likelihood of
    obtaining the data, x and n, for each probability in P.

    Parameters:
    x (int): The number of patients that
    develop severe side effects.
    n (int): The total number of patients observed.
    P (numpy.ndarray): A 1D numpy.ndarray containing
    the various hypothetical probabilities
                    of developing severe side effects.

    Returns:
    numpy.ndarray: A 1D numpy.ndarray containing
    the likelihood of obtaining the data
                for each probability in P.

    Raises:
    ValueError: If n is not a positive integer.
                If x is not an integer greater than or equal to 0.
                If x is greater than n.
                If any value in P is not in the range [0, 1].
    TypeError: If P is not a 1D numpy.ndarray.
    """

    if not isinstance(n, int) or (n <= 0):
        raise ValueError('n must be a positive integer')

    if not isinstance(x, int) or (x < 0):
        raise ValueError(
            'x must be an integer that is greater than or equal to 0')

    if x > n:
        raise ValueError('x cannot be greater than n')

    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError('P must be a 1D numpy.ndarray')

    if np.any(P > 1) or np.any(P < 0):
        raise ValueError('All values in P must be in the range [0, 1]')

    var1 = (np.math.factorial(n))
    var2 = (np.math.factorial(x) * np.math.factorial(n - x))
    factorial = var1 / var2
    factorial *= (np.power(P, x)) * (np.power((1 - P), (n - x)))
    return factorial
