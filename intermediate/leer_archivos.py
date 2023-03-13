#abrir un archivo 
file_txt = open("./data/file.txt")

file_read_all = file_txt.read()
print(f' todo:{file_read_all}')

file_txt.close()

file_txt = open("./data/file.txt")

#volvemos a abrir el archivo (porque se cierra al usar las funciones: read() readlines())
file_readline = file_txt.readline()
print(f' primera: {file_readline}')
print(f' segunda: {file_readline}')
print(f' tercera: {file_readline}') 

file_txt.close()

# volvemos a abrir el archivo
file_txt = open("./data/file.txt")

dict_lines = {0: "a" , 1: "b", 2: "c"}

#agregar el texto a un diccionario
for line in dict_lines:
    dict_lines[line] = file_txt.readline()

print(dict_lines)

file_txt.close()

# para cerrarlo automáticamente y no estar poniendo cada rato un "file.close()"
# podemos colocar:

with open("./data/file.txt") as file_txt:
    for linea in file_txt:
        print(f' \n Esta es una línea usando un with: {linea}')

file_txt = open("./data/file.txt")
for line in dict_lines:
    dict_lines[line] = file_txt.readline()

print(dict_lines)