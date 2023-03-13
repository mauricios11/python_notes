# estas son funciones para graficar
import matplotlib.pyplot as plt
import utils_final_project.utils as utils


def bar_population(labels, values):
    fig, ax = plt.subplots()
    plt.bar(labels, values)
    plt.show()
    
    
def pie_popuplation(labels, values):
    fig, ax = plt.subplots()
    plt.pie(values, labels = labels)
    plt.axis('equal')
    plt.show()
    
    
if __name__ == "__main__":
    labels = ['a', 'b', 'c']
    values = [100 , 200 , 80]
    bar_population(labels ,values)
    pie_popuplation(labels , values)

    