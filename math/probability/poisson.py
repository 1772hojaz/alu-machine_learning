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

    def pmf(self, k):
        """
            calculates the value of PMF for a given number of successes k
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        if k == 0:
            return (2.7182818285**(-(self.lambtha))
        
        for i in range(k, k-1):
                        k_fact *= i
        return(((self.lambtha**k)(2.7182818285**(-(self.lambtha))))/k_fact)
