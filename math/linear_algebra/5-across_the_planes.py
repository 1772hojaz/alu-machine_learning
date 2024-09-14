#!/usr/bin/env python3
"""
this module has a function that adds
two matriceses element-wise
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2Darrays element-wise.

    Args:
    - mat1 (list of ints/floats): The first array.
    - mat2 (list of ints/floats): The second array.

    Returns:
    - list: A new list containing the element-wise sum of arr1 and arr2.
    - None: If mat1 and mat2 are not of the same shape.

    """
    if len(mat1) != len(mat2):
        return None
    for row, row1 in zip(mat1, mat2):
        if len(row) != len(row1):
            return None

    result = [[x + y for x, y in zip(row1, row2)
               ] for row1, row2 in zip(mat1, mat2)]
    return result
