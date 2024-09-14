#!/usr/bin/env python3
"""
this module has a funtion that returns a transpose of a
2D matrix
"""


def matrix_transpose(matrix):
    """Transposes a given matrix.

    Args:
        matrix: A list of lists presenting the matrix.

    Returns:
        transposed matrix as a list.
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed_matrix = []
    for a in range(num_cols):
        row = []
        for b in range(num_rows):
            row.append(matrix[b][a])
        transposed_matrix.append(row)

    return transposed_matrix
