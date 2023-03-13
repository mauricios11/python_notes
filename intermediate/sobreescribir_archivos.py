# """ sobreescribir un archivo.txt """

with open("./data/file.txt", "r+") as file_txt:
    counter = 1
    for line in file_txt:
        print(f' línea {counter}: {line}')
        counter = counter +1

    file_txt.write("Esta es una nueva línea agregada desde el pyfile\n")
    counter = counter +1
    
    """R: no tenemos permisos de escritura. Cuando usamos un open("ruta", "r") 
          solo tenemos permisos de lectura de manera predeterminada
          
        Para agregar permisos, tanto de escritura, como de lectura, podemos especificar como argumento: 'r+'
        Para sobreescribir el contenido del archivo, colocamos como argumento: 'w+'"""


