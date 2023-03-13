# script dentro de la carpeta "package"

def package_func_text_1():
    texto = "Esta es otra función dentro de la carpeta package y contiene texto , agregamos más texto" 
    return texto

def package_func_number_dict():
    numbers = [i * 10 for i in range(1,11)]
    letters = "abcdefjghi"
    
    numbers_dict = { letters[i] : numbers[i] for  i in range(len(numbers))}
    
    return( numbers_dict ) 
    
    

    
