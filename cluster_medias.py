
import matplotlib.pyplot as plt
import numpy as np
import random
puntos=[]
for i in range(50):
    #añade los puntos al array
    puntos.append(random.randint(1,10))
#create an scatter graph with the data of the array
plt.scatter(puntos, puntos)
plt.show()

#print(puntos)
    
