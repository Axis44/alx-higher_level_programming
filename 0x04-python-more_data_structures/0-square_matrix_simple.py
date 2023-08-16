#!/usr/bin/python3
# protottype of square value
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    # matrix lambda square for integers
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
