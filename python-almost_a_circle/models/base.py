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
            base.__nb_objects += 1
            self.id = base.__nb_objects
