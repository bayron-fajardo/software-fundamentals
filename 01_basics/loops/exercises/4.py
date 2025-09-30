"""
Número adivinado: un programa que genera un número aleatorio y
el usuario debe adivinarlo con pistas de "más alto" o "más bajo".
"""

import random

random_number = random.randint(0,3)
adivinado = False

while (adivinado != True):
    
    guess_number = int(input("Ingrese un numero: "))
    if random_number > guess_number:
        print("intenta con un número más alto")
    elif random_number < guess_number:
        print("intenta con un número más bajo")
    else:
        print("Haz adivinado el número")
        adivinado = True