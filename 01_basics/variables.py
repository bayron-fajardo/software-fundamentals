"""
Python Variable Types
---------------------

In Python, variables are dynamically typed (you don’t need to declare their type).
The type depends on the value assigned.
"""

# -------------------------
# Basic Types
# -------------------------

# Integer (int) → whole numbers
x = 10
y = -3
print("Integer:", x, type(x))
print("Integer:", y, type(y))

# Float → decimal numbers
pi = 3.14
g = -9.81
print("Float:", pi, type(pi))
print("Float:", g, type(g))

# String (str) → text
name = "Alice"
greeting = 'Hello'
print("String:", name, type(name))
print("String:", greeting, type(greeting))

# Boolean (bool) → True / False
is_active = True
has_access = False
print("Boolean:", is_active, type(is_active))
print("Boolean:", has_access, type(has_access))

# -------------------------
# Data Structures
# -------------------------

# List → ordered, mutable collection
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, type(fruits))

# Tuple → ordered, immutable collection
point = (10, 20)
print("Tuple:", point, type(point))

# Set → unordered collection of unique elements
unique_numbers = {1, 2, 3, 3}
print("Set:", unique_numbers, type(unique_numbers))  # duplicates removed

# Dictionary → key-value pairs
student = {"name": "Alice", "age": 20}
print("Dictionary:", student, type(student))

# -------------------------
# Special Types
# -------------------------

# NoneType → represents “no value”
result = None
print("NoneType:", result, type(result))

# Complex → numbers with real + imaginary parts
z = 2 + 3j
print("Complex:", z, type(z))

# -------------------------
# Type Checking and Casting
# -------------------------

# Checking type
print("Type of pi:", type(pi))
print("Type of student:", type(student))

# Type casting
num_str = "123"
num_int = int(num_str)     # string → integer
num_float = float(num_str) # string → float
print("Casting str → int:", num_int, type(num_int))
print("Casting str → float:", num_float, type(num_float))
