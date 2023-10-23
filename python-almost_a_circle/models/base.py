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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string for obj"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            else:
                list_dicts = []
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
            f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Json string to dictionary"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
