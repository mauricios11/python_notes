# transformar un string a un booleano
name = "Mauricio"
name_type = type(name)
print('  variable: "{}" tipo: {}'.format(name, name_type))

print("\nsobreescribimos la variable \n")

name = 12
name_type = type(name)
print('  variable: "{}" tipo: {}'.format(name, name_type))

print("\nsobreescribimos la variable \n")

name = True
name_type = type(name)
print('  variable: "{}" tipo: {}'.format(name, name_type))

age = input('Cuál es tu edad? R: ')

print('La edad del usuario es: ' + age)

nombre = input("Cuál es tu nombre? R: ")
print(f'Hola {nombre}. Te voy a decir cuántos años tendrás dentro de 4 años')

edad_mas_4= int(age) + 4
print('Tu edad dentro de 4 años será de: ' + str(edad_mas_4) + ' años :/')
