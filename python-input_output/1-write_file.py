#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """ Write to a file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
