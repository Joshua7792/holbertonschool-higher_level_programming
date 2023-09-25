#!/usr/bin/python3
# Start with the ASCII value of 'a'
ascii_value = ord('a')

# Iterate through the alphabet characters and print them without a new line
for _ in range(26):
    print(chr(ascii_value), end="")
    ascii_value += 1

# Print a new line at the end to separate the output
print()
