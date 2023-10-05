#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = {key: value}  # Create a new dictionary with the key/value pair to update or add
    a_dictionary.update(new_dict)  # Use the update() method to update the input dictionary
    return a_dictionary  # Return the updated dictionary
