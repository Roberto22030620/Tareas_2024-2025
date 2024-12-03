import pandas as pd

df=pd.read_excel('DatosRandom.xlsx')
import matplotlib.pyplot as plt
print(df)
#Crea una grafica de dispersión con los puntos de la columna 'x' y 'y' de df
df.plot.scatter(x='X', y='Y')
plt.show(block=True)
#Se importa la librería KMeans de la librería sklearn.cluster
from sklearn.cluster import KMeans
#Se crea un objeto de la clase KMeans con 3 clusters
kmeans = KMeans(n_clusters=3)
#Se entrena el modelo con los datos de df
kmeans.fit(df)
#Se obtienen los centroides de los clusters
centroids = kmeans.cluster_centers_
#Se obtiene la etiqueta de cada punto
labels = kmeans.labels_
#Se crea una grafica de dispersión con los puntos de la columna 'x' y 'y' de df
#Se asigna un color a cada cluster
colors = ["g.", "r.", "b."]
for i in range(len(df)):
    plt.plot(df['X'][i], df['Y'][i], colors[labels[i]], markersize=10)
#Se grafican los centroides
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=150, linewidths=5, zorder=10)
plt.show(block=True)
#Se importa la librería AgglomerativeClustering de la librería sklearn.cluster
from sklearn.cluster import AgglomerativeClustering
#Se crea un objeto de la clase AgglomerativeClustering con 3 clusters
clustering = AgglomerativeClustering(n_clusters=3)
#Se entrena el modelo con los datos de df
clustering.fit(df)
#Se obtiene la etiqueta de cada punto
labels = clustering.labels_
#Se crea una grafica de dispersión con los puntos de la columna 'x' y 'y' de df
#Se asigna un color a cada cluster
colors = ["g.", "r.", "b."]
for i in range(len(df)):
    plt.plot(df['X'][i], df['Y'][i], colors[labels[i]], markersize=10)
plt.show(block=True)
