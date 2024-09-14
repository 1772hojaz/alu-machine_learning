#!/usr/bin/env python3
"""
this module has a function that adds
two matriceses element-wise
"""


def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2):
        return None

    for row, row1 in zip(mat1, mat2):
        if len(row) != len(row1):
            return None
    result = [x + y for x, y in zip(mat1, mat2)]
    return result
