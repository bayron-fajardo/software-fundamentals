"""
Conditionals Exercises
----------------------

Write Python programs using conditionals (if/elif/else).
Do not use loops unless the exercise specifies it.
"""
# 5. Grade classification.
# Input: a number between 0 and 100.
# Output:
#   - 90–100: "A"
#   - 80–89:  "B"
#   - 70–79:  "C"
#   - 60–69:  "D"
#   - Below 60: "F"

nota = int(input("Ingrese su nota con un entero (0-100): "))

if nota >= 90 and nota <= 100:
    print(f'({nota}) -> 90-100: "A" ')
elif nota >= 80 and nota <= 89:
    print(f'({nota}) -> 80-89:  "B" ')
elif nota >= 70 and nota <= 79:
    print(f'({nota}) -> 70-79:  "C" ')
elif nota >= 60 and nota <= 69:
    print(f'({nota}) -> 60-69:  "D" ')    
else:
    print(f'({nota}) -> <60:    "F" ')
  