#!/usr/bin/python3
""" Module to create a class Student """


class Student:
    """ class tha defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is list:
            i = {}
            for j in attrs:
                if j in self.__dict__:
                    i[j] = self.__dict__[j]
            return i
        else:
            return self.__dict__
