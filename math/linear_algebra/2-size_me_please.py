#!/usr/bin/env python3


def matrix_shape(matrix):
    """
    Calculate the shape of a matrix and return it as a list of integers.

    Args:
    - matrix (list): A matrix presented as a list.

    Returns:
    - list: A list of integers presenting the shape matrix shape
    """
    mat = []
    while isinstance(matrix, list):
        mat.append(len(matrix))
        matrix = matrix[0]
    return mat
