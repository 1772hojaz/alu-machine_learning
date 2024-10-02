#!/usr/bin/env python3
"""
This function calculates ∑(i=1 to n) i²
"""
def summation_i_squared(n):
    """
    Calculate the sum of squares of the first n integers.

    Args:
        n (int): The stopping condition for the summation.
                  Must be a positive integer.

    Returns:
        int: The integer value of the sum of squares from 1 to n.
             Returns None if n is not a valid positive integer.

    Formula used:
        The sum of the squares of the first nintegers is calculated
        using the formula:
        ∑(i=1 to n) i² = n(n + 1)(2n + 1) / 6
    """
    if not isinstance(n, int) or n < 1:
        return None

    return (n * (n + 1) * (2 * n + 1)) // 6
