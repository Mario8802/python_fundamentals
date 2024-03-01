import re

line = input()

pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

names = re.findall(pattern, line)
# without a loop
print(*names)

# Use an Asterisk to Print a List in Python.
# To print a list without commas or square brackets without using a loop,
# you can use the asterisk to unpack the list elements.
# The asterisk operator in Python is known as the unpacking operator.
# You can use it to pull values from iterables, such as lists, strings,
# or tuples.11 Sept 2023
