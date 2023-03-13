x = 3.3
y = 1.1 + 2.2

print (f' valor de "x": {x}')
print (f' valor de "y": {y}\n')
print(f' "x" es mayor a "y":{ x > y}')
print(f' "x" es menor a "y":{ x < y}')
print(f' "x" es igual a "y":{ x == y}')

# hay un problema con la presición de los cálculos con números flotantes

#solución 1: pasar a "y" en formato string y cortarle esos valores
print('\n\nsolución 1: pasarlo a string ".2g"\n' )
y_string = format(y, ".2g")
x_string = str(x)
print(f' tipo: {type(y_string)}')
print(f' "y" al darle "format(y, ".2g")" ha pasado de: \n      ({y}) a ({y_string})')
print(f' ahora comparamos: "y_string" es igual a "x_string"? R: {x_string == y_string}')


print('\n\n solución2: establecer una margen de tolerancia \n')
tolerancia = 0.00001
operacion = abs(x-y)
print(f' El valor absoluto de "x" - "y" es menor a una tolerancia de 0.00001?\n {operacion < tolerancia}')

print('\n\n solución3: redondear el valor\n ')
y_round= round(y,2)
print(f' "x" es igual a "y"(redondeado) ? R: {x == y_round} ')