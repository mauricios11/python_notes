# cálculo que recibe un input, lo opera, y después devuelve el resultado de la operación (output)
# reutilizar código múltiples veces

nombre = "Mauricios"
apellido = "Scobar"

        # estos son parámetros, los que recibe la función para realizar cálculos
def saludo(name, last_name):
    print(f' Mi nombre es: {nombre}')
    print(f' y mi apellido es: {apellido}')
    
#saludo(nombre, apellido)

a_1 = 10
b_1 = 20

def mult( a , b):
    operacion = a * b
    return operacion

def suma( a , b ):
    operacion = a + mult(a_1 , b_1)
    return operacion
        # estos son argumentos, los valores que se utilizan como parámetros dentro de una función
#print(suma(a_1, b_1))





