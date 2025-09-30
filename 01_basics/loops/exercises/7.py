#Sumar digitos de un numero

number = 123455
digitos = [int(d) for d in str(number) ]
suma = 0
for i in range(len(digitos)):
    suma = suma + digitos[i]

print(suma)
    