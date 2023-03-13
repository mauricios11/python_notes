x = True
y = True
u = False
z = False

# usando  el operador AND:
#    para que el operador "and == True" todos los elementos deben de ser "true"

print(f' Si "True" AND "True", entonces: {x and y}')
print(f' Si "True" AND "False", entonces: {x and u}')
print(f' Si "False" AND "False", entonces: {u and z}')

print(f'\n Si "10" es mayor a "5" AND "5" es menor a "10", entonces: {(10>5) and (5<10)}')
print(f' Si "10" es mayor a "5"  AND "5" es mayor a "10", entonces {(10>5) and (5>10)}')

#pedido = int(input("¿Cuántos productos quieres? R: "))
stock = 10

#if pedido <= stock and pedido >=1:
#    print(f'hay elementos suficientes para tu pedido de {pedido} productos')
 
#if pedido < 1:
#    print(f'El mínimo de productos a elegir es 1. no puedes irte sin comprar')
       
#if pedido > stock:
#    print(f'No hay productos suficientes para tu pedido. \n stock actual: {stock} Intenta elegir menos productos')

"********"

# operador OR 
# para que el operador "or == True" al menos uno de los elementos deben de ser "true"""

print(f' Si "True" OR "True", entonces: {x or y}')
print(f' Si "True" OR "False", entonces: {x or u}')
print(f' Si "False" OR "False", entonces: {u or z}')

print(f'\n Si "10" es mayor a "5" OR "5" es menor a "10", entonces: {(10>5) or (5<10)}')
print(f' Si "10" es mayor a "5"  OR "5" es mayor a "10", entonces {(10>5) or (5>10)}')

role = input(" Elige tu rol: ")
print(f' Si role es igual a "admin" OR "user", entonces: {role == "admin" or role == "user"}')
role_true = (role == "admin" or role == "user")
if role_true == True:
    print("Bienvenido al sistema")
else: 
    print(" Para ingresar debes de ser  usuario o admin, sácate de aquí ")
