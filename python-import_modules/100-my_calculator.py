#!/usr/bin/python3
if __name__ == "__main__":
    # Import the required functions from calculator_1.py
    from calculator_1 import add, sub, div, mul
    import sys
    args = sys.argv  # Store the command-line arguments in the 'args' list.

    if len(args) != 4:
        # Check if the number of command-line arguments is not equal to 4.
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)  # Exit the script with an error code of 1.

    # Convert the command-line arguments to integers.
    a = int(args[1])
    operator = args[2]
    b = int(args[3])

    if operator == '+':
        # Check if the operator is addition.
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        # Check if the operator is subtraction.
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        # Check if the operator is multiplication.
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        # Check if the operator is division.
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)  # Exit the script with an error code of 1.
