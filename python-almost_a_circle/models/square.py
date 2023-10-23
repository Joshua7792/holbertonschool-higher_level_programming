#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        """Inizialize new square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Print square info"""
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)
