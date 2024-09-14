#!/usr/bin/env python3
"""
a function that adds tewo arrays element-wise
"""


def add_arrays(arr1, arr2):
    """Adds two matrices element-wise.

    Args:
        arr1: A list of lists representing the first matrix.
        arr2: A list of lists representing the second matrix.

    Returns:
        The sum of the two matrices as a list of lists.

    """
    if len(arr1) != len(arr2):
        return None
    else:
        result = [x + y for x, y in zip(arr1, arr2)]
        return result
