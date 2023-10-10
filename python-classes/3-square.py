#!/usr/bin/python3
"""This module have a class that defines a square """


class Square:
    def __init__(self, size=0):
        """Initialize sqr"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size

    def area(self):
        """Return the area of the square"""
        return self._Square__size ** 2
