#!/usr/bin/env python3

def determinant(matrix):
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        raise TypeError("matrix must be a square matrix")

    if rows == 1 and cols == 1: 
        return matrix[0][0]

    det = 0
    for i in range(rows):
        minor = [row[:i] + row[i+1:] for row in matrix[1:]]
        cof = (-1) ** (i + 1) * determinant(minor)
        det += matrix[0][i] * cof

    return det