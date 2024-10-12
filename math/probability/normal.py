#!/usr/bin/env python3
"""
    Normal distribution
"""


class Normal:
    """
        the class
    """
    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            if stddev < 1:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
                self.mean = float(mean)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = float(sum(data) / len(data))
                self.mean = mean
                summation = 0
                for x in data:
                    summation += ((x - mean) ** 2)
                    stddev = (summation / len(data)) ** (1 / 2)
                    self.stddev = stddev

    def z_score(self, x):
        """
            Calcultes the z-value of a given x value
        """
        z_score = (x - self.mean) / self.stddev
        return z_score

    def x_value(self, z):
        """
            Calculates the x-value given the z-score
        """
        x_value = (z * self.stddev) + self.mean
        return x_value

    def pdf(self, x):
        """
            returns PDF given x-value
        """
        e = 2.7182818285
        pi = 3.1415926536

        pdf = (1 / (self.stddev * ((2 * pi) ** (1 / 2))
                    )) * (e ** (-0.5 * (self.z_score(x) ** 2)))

        return pdf
