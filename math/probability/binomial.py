#!/usr/bin/env python3
"""
    Binomial distribution is a statistical distribution
    that summarizes the probability that a value will take one
    of two independent values under a given set of parameters
    or assumptions.
"""


class Binomial:
    """
        Binomial class
    """
    def __init__(self, data=None, n=1, p=0.5):

        if data is None:
            if n < 1:
                raise ValueError("n must be a positive value")
            else:
                self.n = n
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.p = p
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = float(sum(data) / len(data))
            summation = 0
            for x in data:
                summation += ((x - mean) ** 2)
            variance = (summation / len(data))
            q = variance / mean
            p = (1 - q)
            n = round(mean / p)
            p = float(mean / n)
            self.n = n
            self.p = p

    def pmf(self, k):
        """
            returns the value of the PMF for a given number of successes k
        """

        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        p = self.p
        n = self.n
        q = (1 - p)
        n_factorial = 1
        for i in range(n):
            n_factorial *= (i + 1)
        k_factorial = 1
        for i in range(k):
            k_factorial *= (i + 1)
        nk_factorial = 1
        for i in range(n - k):
            nk_factorial *= (i + 1)
        binomial_co = n_factorial / (k_factorial * nk_factorial)
        pmf = binomial_co * (p ** k) * (q ** (n - k))
        return pmf

    def cdf(self, k):
        '''
            Returns the value of the CDF for a given number of successes
        '''
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        p = self.p
        n = self.n
        q = (1 - p)
        sum = 0
        for i in range(k + 1):
            sum += self.pmf(i)
        cdf = sum
        return cdf
