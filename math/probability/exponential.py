#!/usr/bin/env python3
"""
    The exponential distribution is one of the widely
    used continuous distributions.
    It is often used to model the time elapsed between events.
    We will now mathematically define the exponential distribution,
    and derive its mean and expected value.
    Then we will develop the intuition for the distribution and
    discuss several interesting properties that it has.

"""


class Exponential:
    """
        Explonential distibution class
    """

    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(1 / (sum(data) / len(data)))
