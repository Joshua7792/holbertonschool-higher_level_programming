#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase using ASCII values
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char  # Keep non-lowercase characters as they are
        print(uppercase_char, end="")
    print()  # Print a newline character to end the output
