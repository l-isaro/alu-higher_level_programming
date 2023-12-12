#!/usr/bin/python3
""" This module contains a function that divides
    elements of a matrix by a number """


def matrix_divided(matrix, div):
    """ return a new matrix whose elements have benn divided by div

        args:
            matrix: a list of list that contains integers and floats
            div: a number that will divide all elements of the matrix

        returns:
            a matrix: its elements divided by div"""

    if matrix not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix"\
                        " (list of lists) of integers/floats")

    matrix_size = len(matrix)
    new_matrix = []
    for number in range(matrix_size):
        if len(matrix[number]) != matrix_size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in matrix[number]:
            if type(element) not in (int, float):
                raise TypeError("matrix must be a matrix"\
                                "(list of lists) of integers/floats")
            new_matrix[number].append(element / div)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return new_matrix
