#!/usr/bin/env python3


def matrix_shape(matrix):
    if all(isinstance(submatrix, list) and all(isinstance(row, list) for row in submatrix) for submatrix in matrix):
      blocks = len(matrix)
      rows = len(matrix[0]) if blocks > 0 else 0
      cols = len(matrix[0][0]) if rows > 0 else 0
      mat = [blocks, rows, cols]
      return mat
    else:
        if all(isinstance(row, list) for row in matrix):
            rows = len(matrix)
            cols = len(matrix[0]) if rows > 0 else 0
            mat = [rows, cols]
            return mat