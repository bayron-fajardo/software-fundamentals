"""
Conditionals Exercises
----------------------

Write Python programs using conditionals (if/elif/else).
Do not use loops unless the exercise specifies it.
"""

# 3. Find the largest of three numbers.
# Input: three integer numbers.
# Output: print the largest one.

num1 = int(input("Digite un numero (entero): "))
num2 = int(input("Digite un numero (entero): "))
num3 = int(input("Digite un numero (entero): "))

if num1 > num2 and num1 > num3:
    print(f'{num1} es mayor -> ({num1} > {num2}) y ({num1} > {num3})')
elif num2 > num1 and num2 > num3:
    print(f'{num2} es mayor -> ({num2} > {num1}) y ({num2} > {num3})')
else:
    print(f'{num3} es mayor -> ({num3} > {num2}) y ({num3} > {num1})')
