#!/usr/bin/env python3
"""
A function that deferentiates a polynomials
"""


def poly_derivative(poly):
    """
    Calculate the derivative of a
    polynomial represented by a list of coefficients.

    Args:
        poly (list): A list of coefficients
        representing a polynomial.
                     The index of the list corresponds
                     to the power of x.
                     For example, [5, 3, 0, 1]
                     represents f(x) = 1x^3 + 3x + 5.

    Returns:
        list: A new list of coefficients representing
        the derivative of the polynomial.
              Returns [0] if the derivative is 0 or
              None if the input is invalid.
    """

    if not isinstance(poly, list) or not all(
            isinstance(c, (int, float)) for c in poly):
        return None

    derivative = []

    for i in range(1, len(poly)):
        derivative.append(i * poly[i])

    if not derivative:
        return [0]

    return derivative
