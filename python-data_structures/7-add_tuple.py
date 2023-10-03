#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Append (0, 0) to tuple_a to ensure it has at least two elements
    tuple_a = tuple_a + (0, 0)
    # Append (0, 0) to tuple_b to ensure it has at least two elements
    tuple_b = tuple_b + (0, 0)
    # Perform element-wise addition of tuple_a and tuple_b
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    # Return the result as a new tuple
    return new_tuple
