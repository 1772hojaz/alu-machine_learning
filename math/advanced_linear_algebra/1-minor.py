#!/usr/bin/env python3

"""
A function that calculates the minor matrix of a matrix.
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

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a non-empty square matrix")

    if not matrix or not matrix[0]:
        return 1

    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    if len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for i in range(len(matrix)):
        minor = [row[:i] + row[i + 1:] for row in matrix[1:]]
        cof = (-1) ** i * determinant(minor)
        det += matrix[0][i] * cof
    return det


def minor(matrix):
    """
    Calculates the minor matrix of a given square matrix.

    Args:
        matrix: A list of lists whose minor matrix should be calculated.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square or is empty.

    Returns:
        The minor matrix of the input matrix.
    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    m_len = len(matrix)
    min_matrix = [[0] * m_len for _ in range(m_len)]

    for i in range(m_len):
        for j in range(m_len):
            sub_minor = [row[:j] + row[j + 1:] for k, row in enumerate(
                matrix) if k != i]
            min_matrix[i][j] = determinant(sub_minor)
    return min_matrix
