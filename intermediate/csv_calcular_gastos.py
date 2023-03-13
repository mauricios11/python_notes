import csv
import functools

"""sumar los elementos de la sgunda columna en un dataset"""

# método 1: usando la función sum() y dentro de ella un list comprehension
def read_csv(path):
   # Tu código aquí 👇
   # abrir dataset
   # declarar un reader 
   #hacer un sum con la segunda columna , e iterando con un listcompehension

   return 
           
#método 2: usando un ciclo for 
def sum_gastos_ciclo(path):
     # contado que comienza en 0
     # abrir dataset
     # invocar el reader 
     # ciclo que itera sobre el reader
     # al contador, agregarse a si mismo y al elemento de la columna deseada (elsegundo)
     return 

# método 3: usando reduce
def reduce_sum_gastos(path):
        #abrir elemento
        # invocar reader
        # lista auxiliar
        
        #ciclo que itera sobre variable del reader
        #agregar el elemento de la columna deseado (el segundo)
        # reduce
            
     return 

if __name__ == "__main__":
    
    response = read_csv("./data/gastos.csv")
    print(response)
    suma_1 = sum_gastos_ciclo("./data/gastos.csv")
    print(suma_1)
    suma_reduce = reduce_sum_gastos("./data/gastos.csv")
    print(suma_reduce[1], suma_reduce[0])

# método 1: usando la función sum() y dentro de ella un list comprehension
def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as df: # abrir dataset
        reader = csv.reader(df)# declarar un reader 
        response = sum(int(i[1]) for i in reader)#hacer un sum con la segunda columna , e iterando con un listcompehension

   return response
           
#método 2: usando un ciclo for 
# def sum_gastos_ciclo(path):
#     suma = 0 # contado que comienza en 0
#     with open(path, 'r') as df:# abrir dataset
#        reader = csv.reader(df)# invocar el reader 
#        for row in reader:# ciclo que itera sobre el reader
#            suma = suma + int(row[1])# al contador, agregarse a si mismo y al elemento de la columna deseada (elsegundo)
#     return suma

# método 3: usando reduce
# def reduce_sum_gastos(path):
#     with open(path , 'r') as df:#abrir elemento
#        reader = csv.reader(df)# invocar reader
#        data = [] # lista auxiliar
#        
#        for row in reader: #ciclo que itera sobre variable del reader
#            suma_reduce = functools.reduce(lambda counter, item: counter + item , data) # reduce
#            
#            data.append(int(row[1]))#agregar el elemento de la columna deseado (el segundo)
#     return data , suma_reduce