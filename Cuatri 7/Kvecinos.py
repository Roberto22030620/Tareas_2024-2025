import matplotlib.pyplot as plt
import random
import math

x = []
y = []
for i in range(50):
    x.append(random.randint(1, 10))
    y.append(random.randint(1, 10))

def obtener_distancia():
    distancia = int(input("Ingrese la distancia máxima entre puntos: "))
    if distancia < 2 or distancia > 4:
        print("Distancia no válida, valores permitidos entre 2 y 4")
        distancia = obtener_distancia()
    return distancia
def obtener_clusters():
    cantidad = int(input("Ingrese la cantidad de clusters: "))
    if cantidad < 3 or cantidad > 6:
        print("Cantidad no válida, valores permitidos entre 3 y 6")
        cantidad = obtener_clusters()
    return cantidad
def preguntar_vecinos():
    vecinos = int(input("Ingrese la cantidad de vecinos: "))
    if vecinos < 5:
        print("Vecinos no válidos, valores permitidos mayores a 5")
        vecinos = preguntar_vecinos()
    return vecinos
def calcular_distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def crear_clusters(distancia, clusters, vecinos):
    puntos = list(zip(x, y))
    distancia_euclidiana = {
        (p1, p2): calcular_distancia_euclidiana(p1, p2) for p1 in puntos for p2 in puntos if p1 != p2
    }
    
    clusters_creados = []
    while puntos and len(clusters_creados) < clusters:
        cluster = []
        punto_inicial = puntos.pop(0)
        cluster.append(punto_inicial)
        
        for punto in puntos[:]:
            if distancia_euclidiana.get((punto_inicial, punto), float('inf')) <= distancia:
                cluster.append(punto)
                puntos.remove(punto)
        
        if len(cluster) >= vecinos:
            clusters_creados.append(cluster)
        else:
            puntos.extend(cluster)
    
    if len(clusters_creados) < clusters:
        print("No se pudieron crear suficientes clusters con los vecinos requeridos.")
    
    return clusters_creados


def graficar_clusters(clusters):
    colores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, cluster in enumerate(clusters):
        x_cluster = [p[0] for p in cluster]
        y_cluster = [p[1] for p in cluster]
        plt.scatter(x_cluster, y_cluster, color=colores[i % len(colores)], label=f'Cluster {i+1}')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Clusters')
    plt.legend()
    plt.show()

distancia = obtener_distancia()
cantidad_clusters = obtener_clusters()
vecinos = preguntar_vecinos()
clusters = crear_clusters(distancia, cantidad_clusters, vecinos)

print("Clusters creados:", clusters)
graficar_clusters(clusters)