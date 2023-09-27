#!/usr/bin/python3
# This is a shebang line, specifying the path to the Python interpreter
# that should be used to execute the script.

if __name__ == "__main__":
    import sys
    # Import the sys module to work with command-line arguments.

args = len(sys.argv)
# Calculate the number of arguments provided when running the script.

if args == 1:
    # Check if there is only one argument, which is the script name itself.
    print("0")
    # print "0" to indicate that there is no sum to compute.
else:
    sum = 0
    # Initialize a variable 'sum' to store the total sum of the arguments.
    for i in range(1, args):
        # Loop through the command-line arguments starting from index 1.
        # Index 0 is the script name, so we skip it.
        sum += int(sys.argv[i])
        # Convert argument to an integer using int() and add it to the 'sum'.

    print("{}".format(sum))
    # Print the computed sum of the command-line arguments.
