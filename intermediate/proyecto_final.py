# cargar el dataset y graficar los datos de un país

import csv
import matplotlib.pyplot as plt
import utils_final_project.utils as utils
from utils_final_project import graficas
from utils_final_project import read_csv as read



def plot_bar_countries():
    data = read.read_csv("./data/data_population.csv")
    country = input('Type country: ').title()
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels , values = utils.get_population(country)
        
        graficas.bar_population(labels, values)

def plot_pie():
    data = read.read_csv("./data/data_population.csv")
    data_filtered = list(filter(lambda x : x["Continent"] == "Europe", data))
    labels , values = utils.get_porcentaje(data_filtered)
    
    fig, ax = plt.subplots()
    ax.pie(values , labels = labels)
    plt.show()
    
def plot_propotion():
    df = read.read_csv('./data/data_population.csv')
    data = df.copy()
    
    #filtrar por región
    data = list(filter(lambda x : x['Continent'] == "North America", data))
    
    countries = list(map(lambda x : x['Country/Territory'], data)) #seleccionar sólo la columna "paises"
    porcentaje = list((map(lambda x : x['World Population Percentage'], data)))  # seleccionar solo la columna porcentaje
    
    graficas.pie_popuplation(countries , porcentaje)

if __name__ == "__main__":
    #plot_bar_countries()
    #plot_propotion()
    plot_pie()
    
    
    


    

    
    
    
            

