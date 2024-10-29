import pandas as pd

df=pd.read_excel('DatosRandom.xlsx')
import matplotlib.pyplot as plt
plt.ion()
#print(df)
#Crea una grafica de dispersión con los puntos de la columna 'x' y 'y' de df
df.plot.scatter(x='X', y='Y')
plt.show()
from sklearn.cluster import KMeans
#Crea un objeto KMeans con 3 clusters
kmeans = KMeans(n_clusters=3)
#Ajusta el modelo de kmeans a los puntos de df
kmeans.fit(df)
#Obtiene los centroides de los clusters
centroids = kmeans.cluster_centers_
#Obtiene los labels de los clusters
labels = kmeans.labels_
print(centroids)
print(labels)
#Crea una grafica de dispersión con los puntos de la columna 'x' y 'y' de df
#y colorea los puntos de acuerdo a los labels
df.plot.scatter(x='X', y='Y', c=labels, cmap='viridis')
#Dibuja los centroides de los clusters
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.5)
plt.show()