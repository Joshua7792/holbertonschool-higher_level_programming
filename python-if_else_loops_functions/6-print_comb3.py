#!/usr/bin/python3
# Use two loops to generate combinations of two digits
for first_digit in range(0, 9):
    for second_digit in range(first_digit + 1, 10):
        # Print the combination with a comma and space
        print("{:02d}, ".format(first_digit * 10 + second_digit), end="")
    else:
        # print the last combination without a comma and space
        print("{:02d}".format(first_digit * 10 + second_digit), end="")

# Print a newline character to end the output
print()
