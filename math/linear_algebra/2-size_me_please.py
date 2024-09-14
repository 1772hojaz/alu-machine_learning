#!/usr/bin/env python3


def matrix_shape(matrix):
    if all(isinstance(submatrix, list) and all(isinstance(row, list) for row in 
                                               submatrix) for submatrix in matrix):
        blocks = len(matrix)
        rows = len(matrix[0]) if blocks > 0 and isinstance(
                matrix[0], list)  else 0
        cols = len(matrix[0][0]) if rows > 0 and isinstance(
                matrix[0][0], list) else 0
        return [blocks, rows, cols]
    else:
        if all(isinstance(row, list) for row in matrix):
            rows = len(matrix)
            cols = len(matrix[0]) if rows > 0 and isinstance(
                    matrix[0], list) else 0
            return [rows, cols]
