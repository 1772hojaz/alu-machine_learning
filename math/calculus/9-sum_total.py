#!/usr/bin/env python3

def summation_i_squared(n):
    if not isinstance(n, int) or n < 1:
        return None

    x = 0
    for i in range(1, n + 1):
        x += i**2

    return x
