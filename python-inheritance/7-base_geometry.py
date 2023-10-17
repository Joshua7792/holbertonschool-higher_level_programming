#!/usr/bin/python3
""" Defines a class BaseGeometry """


class BaseGeometry:
    """ define a class BaseGeometry """
    def area(self):
        """ raises an exception """
        raise Exception("area(0 is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value
