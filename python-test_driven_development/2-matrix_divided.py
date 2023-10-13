#!/usr/bin/python3
""" This module contains a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix. """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
    return [[round(element / div, 2) for element in row] for row in matrix]
