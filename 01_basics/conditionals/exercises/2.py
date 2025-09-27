"""
Conditionals Exercises
----------------------

Write Python programs using conditionals (if/elif/else).
Do not use loops unless the exercise specifies it.
"""
# 2. Determine if a number is even or odd.
# Input: an integer number.
# Output: print "Even" or "Odd".

n = int(input("Ingrese un numero (Entero) para verificar si es par o impar: "))

if n % 2 == 0:
    print(f'{n} es par')
else:
    print(f'{n} es impar')