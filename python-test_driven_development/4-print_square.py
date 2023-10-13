#!/usr/bin/python3
"""Defines a function that prints a square with the character #."""


def print_square(size):
    """
        Function that print a square with '#'
        size - is the size lenght of the square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print("#" * size)
