#!/usr/bin/env python3
"""
 a function that performs matrix multiplication

"""


def mat_mul(mat1, mat2):
    """
    You can assume that mat1 and mat2 are
    2D matrices containing ints/floats
    You can assume all elements in the same dimension
    are of the same type/shape
    You must return a new matrix
    If the two matrices cannot be multiplied, return None
    """
    rows_mat1, cols_mat1 = len(mat1), len(mat1[0])
    rows_mat2, cols_mat2 = len(mat2), len(mat2[0])

    if cols_mat1 != rows_mat2:
        return None

    result = [[0] * cols_mat2 for _ in range(rows_mat1)]

    for i in range(rows_mat1):
        for j in range(cols_mat2):
            result[i][j] = sum(
                    mat1[i][k] * mat2[k][j] for k in range(cols_mat1))

    return result
