number = int(input("Ingrese un numero"))

for i in range(number):
    print("*"*(i+1))

for j in range(number):
    print("*"*(number-j))