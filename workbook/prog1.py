#!/anaconda2/bin/python
# prog1.py

# import sys

# Output arguments to console
# dog1 = sys.argv[1]
# dog2 = sys.argv[2]
# print("I hate " + dog1 + ", but I love " + dog2 + "!")

# Add these numbers
# num1 = float(sys.argv[1])
# num2 = float(sys.argv[2])

# total = num1 + num2
# print(total)

#!/usr/bin/env python

import sys
import re

# Exit program with usage output
# def exit_with_usaage():
#   print("")
#   print("Usage: {} <arg1> <arg2>".format(sys.argv[0]))
#   exit(0)

# # check length of sys args
# def check_length(length):
#   if int(len(sys.argv)) != length:
#     print("Error: two arguments required.")
#     exit_with_usaage()

# # Check if values are a number
# def check_if_number(value, message):
#   isNumber = r'^[1-9][0-9]*\.?[0-9]*([Ee][+-]?[0-9]+)?$';

#   if not re.search(isNumber, value):
#     print(message)
#     exit_with_usaage()

# check_length(3)
# check_if_number(sys.argv[1], 'Error: the first argument must be a number')
# check_if_number(sys.argv[2], 'Error: the second argument must be a number')

# a = float(sys.argv[1])
# b = float(sys.argv[2])

# print (a + b)


# try:
#   s = "first"
#   a = float(sys.argv[1])
#   s = "second"
#   b = float(sys.argv[2])
# except ValueError:
#   print("Error: the %s argument must be a number" % s)
# except IndexError as err:
#   print(err)

# # print("OK!")
# print (a + b)

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
val_floats = [float(n) for n in lst]
print(lst)
print(val_floats)







