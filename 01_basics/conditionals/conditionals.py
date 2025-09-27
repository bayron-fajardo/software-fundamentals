"""
Conditionals and Loops in Python
--------------------------------
Basic examples of decision making (if/else) and repetition (for/while).
"""

# -------------------------
# Conditionals
# -------------------------

age = 18

if age < 18:
    print("You are underage.")
elif age == 18:
    print("You just turned 18!")
else:
    print("You are an adult.")

# Nested conditionals
number = -5
if number >= 0:
    if number == 0:
        print("Number is zero.")
    else:
        print("Number is positive.")
else:
    print("Number is negative.")