"""
Conditionals Exercises
----------------------

Write Python programs using conditionals (if/elif/else).
Do not use loops unless the exercise specifies it.
"""
# 4. Check if a year is a leap year.
# Rules:
# - A year is leap if divisible by 4,
# - but not divisible by 100 unless also divisible by 400.


anio = int(input("Digite un año para verificar si es un año bisciesto: "))

if anio % 400 == 0:
    print(anio, "es un año bisiesto")
elif anio % 100 == 0:
    print(anio, "NO es un año bisiesto")
elif anio % 4 == 0:
    print(anio, "es un año bisiesto")
else:
    print(anio, "NO es un año bisiesto")