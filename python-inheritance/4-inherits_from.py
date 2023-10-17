#!/usr/bin/python3
"""Defines a function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class; otherwise False."""


def inherits_from(obj, a_class):
    """ Returns True if the object is an instance of
    a class that inherited (directly or indirectly)"""
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        False
