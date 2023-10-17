#!/usr/bin/python3
"""Defines a function that returns True if the object is an instance of"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
