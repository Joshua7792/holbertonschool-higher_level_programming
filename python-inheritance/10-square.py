#!/usr/bin/python3
"""Square class inherited from Rectangle class"""


rectangle = __import__('9-rectangle').Rectangle


class Square(rectangle):
    def __init__(self, size):
        """Square class inherited from Rectangle class"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Square class inherited from Rectangle class"""
        return self.__size * self.__size
