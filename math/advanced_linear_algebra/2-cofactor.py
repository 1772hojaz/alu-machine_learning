#!/usr/bin/env python3
"""
This fuction calculates the cofactor of a matrix
"""


def determinant(matrix):
    """
    Calculates the determinant of a square matrix.

    Args:
        matrix: A list of lists whose determinant should be calculated.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square.

    Returns:
        The determinant of the matrix.
    """

    if not all(isinstance(x, list) for x in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or not matrix[0]:
        return 1

    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    det = 0
    for i in range(len(matrix)):
        minor = [row[:i] + row[i+1:] for row in matrix[1:]]
        cof = (-1) ** i * determinant(minor)
        det += matrix[0][i] * cof
    return det


def cofactor(matrix):
    """
    Calculates the cofactor matrix of a given matrix.

    Args:
    matrix: A list of lists whose cofactor matrix should be calculated.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.

    Returns:
        The cofactor matrix of the input matrix.
    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or not matrix[0]:
        return 1

    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return matrix[0][0]
    cof = 0
    for i in range(len(matrix)):
        minor = [row[:i] + row[i+1:] for row in matrix[1:]]
        cof = (-1) ** i * determinant(minor)

    cof_matrix = [[0] * len(matrix) for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            minor = [row[:j] + row[j + 1:] for k, row in enumerate(
                matrix) if k != i]
            cof_matrix[i][j] = ((-1) ** (i + j)) * determinant(minor)
    return cof_matrix
