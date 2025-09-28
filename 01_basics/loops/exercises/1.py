"""
Pide un número al usuario y 
muestra su tabla de multiplicar 
del 1 al 10.
"""
number = int(input("Digite un número para ver su tabla de multiplicar: "))

for i in range(10):
    i+=1
    print(f"{number}X{i}={number*i}")