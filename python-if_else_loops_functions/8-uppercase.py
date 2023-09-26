#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase using ASCII values
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()  # Print a newline character to end the output
