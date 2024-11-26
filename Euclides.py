import matplotlib.pyplot as plt
#import numpy as np
import random
x=[]
y=[]
for i in range(50):
    x.append(random.randint(1,10))
    y.append(random.randint(1,10))

def obtener_distancia():
    distancia=int(input("Ingrese la distancia máxima entre puntos: "))
    if distancia < 2 or distancia > 4:
        print("Distancia no válida, valores permitidos entre 2 y 4")
        distancia=obtener_distancia()
    return distancia
def obtener_clusters():
    cantidad=int(input("Ingrese la cantidad de clusters: "))
    if cantidad < 3 or cantidad > 6:
        print("Cantidad no válida, valores permitidos entre 3 y 6")
        cantidad=obtener_clusters()
    return cantidad
def graficar(cantidad, distancia, x, y):
    print("Clusters:", cantidad)
    print("Distancia:", distancia)
    plt.scatter(x, y)
    #define centros de los clusters aleatoriamente, muestra el centro con un color diferente y crea una circunferencia con la distancia
    for i in range(cantidad):
        centro_x=random.randint(1,10)
        centro_y=random.randint(1,10)
        plt.scatter(centro_x, centro_y, c='red')
        circulo=plt.Circle((centro_x, centro_y), distancia, color='red', fill=False)
        plt.gcf().gca().add_artist(circulo)
    ####queda pendiente preguntar a chat qué hace esto para poder explicarlo
    plt.show()
    return 0

graficar(obtener_clusters(), obtener_distancia(), x, y)