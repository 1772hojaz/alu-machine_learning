#!/usr/bin/env python3


def matrix_shape(matrix):
    """
      Args:
      -a matrix presented as a list

      Returns:
      - returs a list of integers presennting the matrix shape.
    """
    mat = []
    while isinstance(matrix, list):
        mat.append(len(matrix))
        matrix = matrix[0]
    return mat
