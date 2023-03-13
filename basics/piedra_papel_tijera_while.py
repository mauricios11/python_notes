# piedra papel ó tijera
''' establecer una opción donde se elija la de rondas a jugar
    El jugador que haya ganado más veces será el ganador de la ronda'''

import random

options = ["piedra", "papel", "tijera"]

print("Vamos a jugar a piedra, papel ó tijera:")
user_name = input("Escribe tu nickname: ")
print("Instrucciones: \n (1)No escribas los números como palabras") 
print(" (2) tampoco una cantidad mayor a 5 rondas ni menor a 2 ")

rondas = input(f"\n Hola {user_name}.\n Cuántas rondas se tendrán que ganar para se el triunfador definitivo? R: ").replace("-","")

#Si no es un dígito
if rondas.isdigit() == False:
    print("El número elegido debe estar escrito en dígitos, no como una palabra")
    print("\n\n volvamos a comenzar")
    exit()
    
rondas = int(rondas)
# si está fuera del rango
if not rondas in range(2,6):
    print(f"Has escrito: {rondas}")
    print("Tu número está fuera del rango. Elegir uno que esté entre [2,5]")
    print("\n\n volvamos a comenzar")


ronda = 1
user_wins = 0
machine_wins = 0

while True:
    if machine_wins > user_wins and machine_wins >= rondas:
            print(f' computadora ha ganado el juego con {machine_wins} puntos!')
            break
    
    if machine_wins < user_wins and user_wins >= rondas:
            print(f' {user_name} ha ganado el juego con {user_wins} puntos!')
            break
        
    if ronda > 1:
        print(f' \n * * * puntos: computadora => {machine_wins} {user_name} => {user_wins}\n')
        
    print("* "*10)
    print(f' ronda: {ronda}')
    print("* "*10)
    
    user = input("Elige una opción entre [piedra][papel][tijera]: ").lower().replace(" ", "")
    machine = random.choice(options)
    ronda += 1 
    print(f' elección de {user_name}: {user} elección de la computadora: {machine}')
    
    if user in options:
        while user == machine:
            print("Empate! \n volvamos a jugar para el desempate")
            user = input("Elige una opción entre las tres posibles: ").lower().lstrip()
            machine = random.choice(options)
            
            
        if user == "piedra":
            if machine == "tijera":
                print(f" {machine} le gana a la {user} La computadora gana!")
                machine_wins += 1

            else:
                #papel
                print(f" {user} le gana al {machine}  {user_name} gana!") 
                user_wins += 1       
                
        elif user == "papel":
            if machine == "piedra":
                print(f" {user} le gana a la {machine}  {user_name} gana!")
                user_wins += 1

            else:
                #tijera
                print(f" {machine} le gana al {user} La computadora gana!")
                machine_wins += 1

        
        elif user == "tijera":
            if machine == "papel":
                print(f" {user} le gana al {machine}  {user_name} gana!")
                user_wins += 1
                #piedra
            else:
                print(f" {machine} le gana a la {user}  La computadora gana!")
                machine_wins += 1
                
   
    else:
            print("favor de elegir una opción válida")
            continue
    
      
        
print(f'\n gracias por jugar ')
            
    




