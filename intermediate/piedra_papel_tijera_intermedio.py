# hacer un juego de piedra papel ó tijera 

import random

"""piedra gana a tijera,
   tijera gana a papel,
   papel gana a piedra"""



saludo = """*** Juguemos a piedra papel ó tijera ***\n
 Reglas al elegir una opción:\n 
 (1) Si hay un empate, nadie gana puntos y se deberá de jugar una vez más
 (2) Es posible seleccionar la cantidad de rondas ganadas para ser el triunfador definitivo. 
     El mínimo es de 2 y el máximo es de 5\n"""

opciones = ["piedra", "papel", "tijera"]
user_wins = 0
machine_wins = 0
  
#limpiamos el input del usuario:
def limpiar_acentos_y_caracteres(texto):
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
               'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
               'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
               'ã': 'a', 'õ': 'o'}
    caracteres_list = [",", "_", ".", "-", "=", "+", "?", "!", "%", "/", "*" ," "]
    
    for letra in acentos:
        if letra in acentos:
            texto = texto.replace(letra, acentos[letra])
    
    for letra in caracteres_list:
        if letra in caracteres_list:
            texto = texto.replace(letra, "")
            
    return texto 

def name_and_intentos_func():
    user_name = input("elige tu nickname: ").lower().replace(" ", "")
    while True:
        prohibido = ["hola", "ola", "aloh", "alo", "h", "hh", "hhola"]
        if user_name in prohibido:
            user_name = input(f'Hola, cómo estás? Escribe un pinche nombre y no me saludEs! >:[  ').lower().replace(" ", "")
        else:
            break
        
    intentos = int(input("Cuántas rondas se deberán jugar para definir un ganador? R: "))
    
    if not intentos in range(2,6):
        print(f' Favor de elegir una cantidad de rondas válida. Volvamos a empezar.')
        exit()
    return user_name, intentos

def user_election_func():
    user = input("Elige una opción [piedra] [papel] [tijera]: ").lower()
    user = limpiar_acentos_y_caracteres(user)
    
    if user in opciones:
        return user
    
    else:
        print('\n Esta opción => "{}" no es válida. Favor de elegir [piedra] [papel] [tijera]'.format(user.upper()))
        return None
    
def empate(user, machine):
    if user == machine:
        return print('Empate! Volvamos juguemos una ronda más para el desempate')

def rules_func(user , machine, user_name):
    global user_wins
    global machine_wins
    
    if user == "piedra":
        if machine == "tijera":
            user_wins += 1
            return print(f' \n{user} le gana a la {machine}, un punto para {user_name}!') , user_wins
            
        if machine == "papel":
            #papel
            machine_wins += 1
            return print(f' \n {machine} le gana a la {user}, un punto para la computadora!'), machine_wins  
                    
    elif user == "papel":
        if machine == "tijera":
            machine_wins += 1
            return print(f' \n {machine} le gana al {user}, un punto para la computadora!'), machine_wins       
        
        if machine == "piedra":
            #piedra
            user_wins += 1 
            return print(f' \n {user} le gana a la {machine}, un punto para {user_name}!'), user_wins      
                    
    elif user == "tijera":
        if machine == "piedra":
           machine_wins += 1
           return print(f' \n{machine} le gana a la {user}, un punto para la computadora!'), machine_wins
       
        if machine == "papel":    
            #papel
            user_wins += 1 
            return print(f' \n{user} le gana al {machine}, un punto para {user_name}!'), user_wins
            
def juego():
    rondas = 1
    print(saludo)
    
    user_name , intentos = name_and_intentos_func()
    
    while True:
        
        print(f'\n *** Ronda {rondas} ***\n')
        if rondas > 1:
            print(f'\n puntaje: {user_name.upper()} => {user_wins}, computadora => {machine_wins}\n')
        rondas += 1
        user = user_election_func()
        machine = random.choice(opciones)
        
        print(f'******** {user_name} a elegido: {user}, la computadora: {machine}')
          
        if empate(user, machine) == True:
            rondas += 1
            continue
        else: 
            rules_func(user, machine, user_name)
        
        if user_wins == intentos or machine_wins == intentos:
            if user_wins > machine_wins:
                print(f' \n{user_name} gana con {user_wins} puntos. MVP! MVP! MVP!')
            else: 
                print(f' \nla computadora gana con {machine_wins} puntos')
            
            print("*** Gracias por jugar ***")
            break

juego()





