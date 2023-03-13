# graficar datos con matplotlib

import matplotlib.pyplot as plt

# función para gráficos de barras 
def barplot(labels , values):
    fig , ax = plt.subplots()
    ax.bar(labels , values)
    plt.show()
    
def pie(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values , labels = labels)
    ax.axis('equal')
    plt.show()
    
if __name__ == "__main__":
    labels = ['a', 'b', 'c']
    values = [100 , 200 , 80]
    barplot(labels ,values)
    pie(labels , values)