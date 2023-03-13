text_titulo = " este es un título"  
text_python = "Ella sabe programar en PythOn!"

print("PythOn" in text_python)
print("java" in text_python)

if "PythOn" in text_python:
    text_jav = text_python.replace("PythOn", "java")
    print(text_jav + "\n" +("*  " * 10))
  
minusculas = text_python.lower()
mayusculas = text_jav.upper()
sin_espacios = text_python.replace (' ', '')
under_score = text_jav.lower().replace(' ', '_')
count_a = text_python.count('a')
count_e = text_jav.count('e')
swap_case = text_python.swapcase()
starts_with = text_python.startswith("Ella")
ends_with = text_jav.endswith("!!")
capitalize_text = text_titulo.lstrip().capitalize()
title_text = text_python.title()
is_digit = "3457".isdigit()


print(f' Cantidad de caracteres en la frase: \n "{text_python}" \n Es de: {len(text_python)}')

print(f' pasamos toda la frase a minúsculas: {minusculas}')
print(f' pasamos toda la frase a mayúsculas: {mayusculas}')

print(f' quitamos los espacios presentes en todo el string : {sin_espacios}\n')
print(f' cambiamos los espacios por underscore, también pasamos todo a minúsculas: {under_score}\n')

print(f' contar las veces que a parece la "a": {count_a}')
print(f' contar las veces que aparece la "e": {count_e}\n')

print(f' pasamos las mayúsculas a minúsculas y viceversa: {swap_case}\n')

print(f' consultamos si el string empieza con una mayúscula: {starts_with}')
print(f' consultamos si el string empieza con una mayúscula: {ends_with}\n')

text_titulo = " este es un título"

print(f' quitamos los "_espacios_": antes de la primera letra del string y después de la última.')
print(f' también cambiamos la primera letra del string por una minúscula: {capitalize_text}')
print(f'\n convertimos en "título" el string:')
print(f' (pasamos a mayúsculas las primeras letras de cada palabra)-> {title_text}')

print(f' \n reconocer si un elemento es un dígito. Con un string: "{is_digit}" y con un entero: no se puede')