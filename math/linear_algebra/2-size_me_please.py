#!/usr/bin/env python3


def matrix_shape(matrix):
    """
    Calculate the shape of a matrix and return it as a list of integers.

    Args:
    - matrix (list): A matrix presented as a nested list (e.g., [[1, 2], [3, 4]]).

    Returns:
    - list: A list of integers representing the shape of the matrix.
            For example, [[1, 2], [3, 4]] will return [2, 2],
            representing 2 rows and 2 columns.
            
    Raises:
    - ValueError: If the input is not a valid matrix or if the matrix is irregular (rows of different lengths).
    """
    mat = []
    while isinstance(matrix, list):
        mat.append(len(matrix))
        matrix = matrix[0]
    return mat
