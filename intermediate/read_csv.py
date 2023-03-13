# abrir un csv por medio de python (sin usar pandas)

import csv

def read_header(path):
    with open(path, 'r') as df: # abrimos el csv
        reader = csv.reader(df, delimiter = ",") # leemos el csv
        header = next(reader) # definimos los headers y los imprimimos
        print(header)
       #for row in reader: # ciclo que itera sobre la función => csv.reader()
        #    print('***' *5)
         #   print(row)
            

"""Queremos la oposibilidad de ejecutarlo como un script, ó como un módulo, para tener ambas opciones usamos:"""

def read_csv(path):
    with open(path, "r") as df:
        reader = csv.reader(df, delimiter= ",")
        header = next(reader)
        for row in reader:
            iterador = list(zip(header , row))
            print(iterador)

def create_df_dict(path):
    with open(path, 'r') as df:
        reader = csv.reader(df, delimiter= ',')
        header = next(reader)
        for row in reader:
            iterador = zip(header, row)
            #print(list(iterador))
            country_dict_df = { header : row for header, row in iterador}
            print(country_dict_df)


""" ahora con lo anterior, creamos una lista de diccionarios"""
def create_df_dict(path):
    with open(path, 'r') as df:
        reader = csv.reader(df, delimiter= ',')
        header = next(reader)
        country_df = []
        
        for row in reader:
            iterador = zip(header, row)
            country_dict_df = dict(iterador)#{ header : row for header, row in iterador}
            country_df.append(country_dict_df)
            
    return country_df




if __name__ == "__main__":
    read_header("./data/data_population.csv")
    #read_csv("./data/data_population.csv")
    #create_df_dict("./data/data_population.csv")
    df_country = create_df_dict("./data/data_population.csv")
    print(df_country[0])
    
    
