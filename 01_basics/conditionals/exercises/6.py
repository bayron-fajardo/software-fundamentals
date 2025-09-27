"""
Conditionals Exercises
----------------------

Write Python programs using conditionals (if/elif/else).
Do not use loops unless the exercise specifies it.
"""
# 6. Check if a person can vote.
# Input: age.
# Output: print "Can vote" if age >= 18, otherwise "Cannot vote".

edad = int(input("Ingrese su edad"))

if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")