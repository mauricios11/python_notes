#Piedra papel ó tijera con uso de tuplas

# piedra vs  papel = papel
# papel vs tijera = tijera
# tijera vs piedra = piedra
"""Juego de piedra papel ó tijera programado en python"""

import random

opciones = ("piedra", "papel", "tijera")
print(" Juguemos a piedra, papel ó tijera")

user_name = input("Cuál es tu nombre? R: ")
user = input("Elige una opción entre las tres posibles: ").lower().replace(" ", "")
machine = random.choice(opciones)
print(f' elección de {user_name}: {user} elección de la computadora: {machine}')

if user in opciones:
    while user == machine:
        print("Empate! \n volvamos a jugar para el desempate")
        user = input("Elige una opción entre las tres posibles: ").lower().lstrip()
        machine = random.choice(opciones)
        print(f' elección de {user_name}: {user} elección de la computadora: {machine}')
        

    if user == "piedra":
        if machine == "tijera":
            print(f" {machine} le gana a la {user} \n La computadora gana!")
        else:
            #papel
            print(f" {user} le gana al {machine} \n {user_name} gana!") 

    elif user == "papel":
        if machine == "piedra":
            print(f" {user} le gana a la {machine} \n {user_name} gana!")
        else:
            #tijera
            print(f" {machine} le gana al {user} \n La computadora gana!")
    
    elif user == "tijera":
        if machine == "papel":
            print(f" {user} le gana al {machine} \n {user_name} gana!")
            #piedra
        else:
            print(f" {machine} le gana a la {user} \n La computadora gana!")
        
    
else:
    print("favor de elegir una opción válida")
    

    