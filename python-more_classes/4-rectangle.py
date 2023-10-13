#!/usr/bin/python3
"""Module that defines a class"""


class Rectangle:
    """Definition of rectangle attribute"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = height
            self.__width = width

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        result_area = self.__width * self.__height
        return result_area

    def perimeter(self):
        """Retrieve the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            res_perimeter = 0
            return res_perimeter
        else:
            res_perimeter = (self.__width * 2) + (self.__height * 2)
            return res_perimeter

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i < self.__height - 1:
                rect += "\n"  # Add a newline except for the last row
        return rect

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
