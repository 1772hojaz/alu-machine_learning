#!/usr/bin/env python3

def determinant(matrix):

    if not all(isinstance(x, list) for x in matrix):
        raise TypeError("matrix must be a list of lists")
    #0x0 matrix
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