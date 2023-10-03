#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the current row
        for i in range(len(row)):
            # Check if the current element is not the last element in the row
            if i != len(row) - 1:
                # Print the current integer with formatting and add a space
                print("{:d}".format(row[i]), end=" ")
            else:
                # If it's the last element in the row, just print the integer
                print("{:d}".format(row[i]))
