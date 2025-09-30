#   Factorial
#   5! = 1X2X3X4X

num = 5
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
    i+=i


print(factorial)