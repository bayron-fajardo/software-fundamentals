"""
Conditionals Exercises
----------------------

Write Python programs using conditionals (if/elif/else).
Do not use loops unless the exercise specifies it.
"""
# 7. Write a program that asks for a password.
# If the password is "admin123", print "Access granted".
# Otherwise, print "Access denied".

admin_pass = "admin123"
input_pass = input("Ingrese la contraseña: ")
if input_pass == admin_pass:
    print("Access granted")
else:
    print("Access denied")