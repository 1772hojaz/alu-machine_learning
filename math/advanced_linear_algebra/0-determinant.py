#!/usr/bin/env python3

def determinant(matrix):
    """
    A function determinant(matrix) -  That calculates the determinant
    matrix is a list of lists whose determinant should be calculated
    If matrix: is not a list of lists, raise a TypeError with the
    message matrix must be a list of lists
    If matrix:  is not square, raise a ValueError with the message
      matrix must be a square matrix
    The list [[]] represents a 0x0 matrix

    Returns: the determinant of matrix
    """

    if not all(isinstance(x, list) for x in matrix):
        raise TypeError("matrix must be a list of lists")
    # 0x0 matrix
    if not matrix or not matrix[0]:
        return 1

    # square matrix
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    # Cofactor
    det = 0
    for i in range(len(matrix)):
        minor = [row[:i] + row[i+1:] for row in matrix[1:]]
        cof = (-1) ** i * determinant(minor)
        det += matrix[0][i] * cof
    return det
