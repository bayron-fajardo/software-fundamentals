"""
Conditionals Exercises
----------------------

Write Python programs using conditionals (if/elif/else).
Do not use loops unless the exercise specifies it.
"""

# 1. Check if a number is positive, negative, or zero.
# Input: an integer number.
# Output: print whether it is positive, negative, or zero.

n = int(input("enter an integer number (+,-,0): "))
if n >= 0:
    if n == 0:
        print('Zero')
    else:
        print(f'{n} is postive.')
else:
    print(f'{n} is negative')
