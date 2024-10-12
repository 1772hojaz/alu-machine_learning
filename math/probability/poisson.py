#!/usr/bin/env python3
"""
    The formula for Poisson distribution is f(x) = P(X=x) = (e-λ λx )/x!.
    For the Poisson distribution, λ is always greater than 0.
    For Poisson distribution, the mean and the variance of the
    distribution are equal.
"""


class Poisson:
    """
        Poisson Class
    """
    def __init__(self, data=None, lambtha=1):
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(sum(data) / len(data))

    def k_fact(self, a):
        """
        Calculates the factorial
        """
        if a < 0:
            return 0
        if a == 0 or a == 1:
            return 1
        return a * self.k_fact(a - 1)

    def pmf(self, k):
        """
            calculates the value of PMF for a given number of successes k
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        x = ((self.lambtha ** k) * (e ** -self.lambtha)) / self.k_fact(k)
        return x

    def cdf(self, k):
        """
        calculates the value of CDF for a given number of successes k.
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        e = 2.7182818285

        for i in range(k + 1):
            cdf += ((e ** -self.lambtha) * (self.lambtha ** i)
                    ) / self.k_fact(i)
        return cdf
