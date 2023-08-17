#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    # square matrix using lambda
    return list(map(lambda row: list(map(lambda col: col**2, row)), matrix))
