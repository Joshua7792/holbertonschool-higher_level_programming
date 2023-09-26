#!/usr/bin/python3
# Use two loops to generate combinations of two digits
for first_digit in range(0, 10):
    for second_digit in range(first_digit + 1, 10):
        # Check if it's the last combination and print accordingly
        if first_digit == 8 and second_digit == 9:
            print("{:02d}".format(first_digit * 10 + second_digit), end="")
        else:
            print("{:02d}, ".format(first_digit * 10 + second_digit), end="")
# Print a newline character to end the output
print()
