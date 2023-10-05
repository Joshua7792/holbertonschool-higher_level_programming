#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)  # Set() removes duplicates
    return sum(unique_list)  # Sum() adds all elements in a list
