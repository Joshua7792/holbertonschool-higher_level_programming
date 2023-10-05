#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)  # Use the pop() method to remove the key/value
    return a_dictionary  # Return the updated dictionary
