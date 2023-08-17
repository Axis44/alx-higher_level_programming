#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    # square matrix using lambda
    return list(map(lambda x: list(map(lambda t: t**2, x)), matrix))
