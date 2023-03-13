if True:
    print(f"condicional if = True: Siempre se ejecuta")
    
if False:
    print("condicional if  = False: no se ejecuta")
    
#mascota = input("Cuál es tu mascota favorita? R: ")
#mascota = mascota.lower()

""" if mascota == "gato" or mascota == "perro":
    print(" Tu mascota es mascoteable")
    if mascota == "perro":
        print("Tu mascota viene de la familia taxonómica de los caninos y debería llamarse firualis")
        
    if mascota == "gato":
        print("Tu mascota viene de la familia taxonómica de los felinos y no debería de llamarse firulais. Es raro.")
    
    if mascota == "pez":
        print("Felicidades! tu mascota es deliciosa :P")
else: 
    print(" Tu mascota no es mascoteable, devuélvela")
     """
num = int(input("Escribe un número para saber si es par ó impar: "))

if num % 2 != 0:
    print('El número elegido: "{}" es un número impar'.format(num))
    
else: 
    print('El número elegido: "{}" es un número par'.format(num))
    

        