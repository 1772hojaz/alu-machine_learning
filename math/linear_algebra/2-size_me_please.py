#!/usr/bin/env python3


# def matrix_shape(matrix):
#     if all(isinstance(submatrix, list) and
# all(isinstance(row, list) for row in
# submatrix) for submatrix in matrix):
#         blocks = len(matrix)
#         rows = len(matrix[0]) if blocks > 0 else 0
#         cols = len(matrix[0][0]) if rows > 0 else 0
#         mat = list((blocks, rows, cols))
#         return mat
#     else:
#         if all(isinstance(row, list) for row in matrix):
#             rows = len(matrix)
#             cols = len(matrix[0]) if rows > 0 else 0
#             mat = list((rows, cols))
#             return mat

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
