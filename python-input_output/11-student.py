#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Define a Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation
        of the Student class """
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                if str(i) == "first_name":
                    new_dict[i] = self.first_name
                elif i == "last_name":
                    new_dict[i] = self.last_name
                elif i == "age":
                    new_dict[i] = self.age
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            elif key == "last_name":
                self.last_name = value
            elif key == "age":
                self.age = value
