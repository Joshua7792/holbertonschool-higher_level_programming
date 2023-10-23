#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Return the area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Display rectangle in STDOUT"""
        # Print empty lines (spaces) for the 'y' coordinate
        for i in range(self.__y):
            print()
        # Print each row of the rectangle
        for i in range(self.__height):
            # Print empty spaces (offset) for the 'x' coordinate
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Print the rectangle info """
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        argc = len(args)
        attrs = ["id", "width", "height", "x", "y"]
        kwargc = len(kwargs)
        if argc > 0:
            for i in range(argc):
                setattr(self, attrs[i], args[i])
        elif kwargc > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

