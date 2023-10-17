#!/usr/bin/python3
""" Defines a function that returns True if the object is an instance of"""


def inherits_from(obj, a_class):
    """ Returns True if the object is an instance of"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        False
