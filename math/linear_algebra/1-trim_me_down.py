#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
for i in range(3):
    arr = [matrix[i][3], matrix[i][4]]
    the_middle += [arr]
print("The middle columns of the matrix are: {}".format(the_middle))
