#!/usr/bin/python3
""" Base class """

import json
import csv
from os import path


class Base:
    """ Base for other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
