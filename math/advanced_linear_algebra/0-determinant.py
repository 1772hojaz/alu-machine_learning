#!/usr/bin/env python3

def determinant(matrix):
    col = len(matrix[0]
    rows = len(matrix)
    if all(isinstance(item, list) for item in matrix):
              if rows != col :
                    raise TypeError("matrix must be a square matrix")
              else:
                    #using the cofactor method
                    det = 0
                    if col = 1 and rows = 1 :
                        return matrix[0][0]
                    else:
                        for i in range(rows):
              minor = [row[:i] + row[i+1:] for row in matrix[1:]
                            cof = (-1) ** (i + 1) * determinant(minor)
                       det = + matrix[0][i] * cof
    else:
        raise TypeError("matrix must be a list of lists")
