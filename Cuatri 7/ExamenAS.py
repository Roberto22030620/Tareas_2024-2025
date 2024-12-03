import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel("Datos_cluster_rlm.xlsx")
#Nombres de columnas:
#df["Horas de estudio"] i1=x
#df["Calificacion examen anterior"] i2=y
#df["Calificacion de examen futuro"] d=a
df=df.rename(columns={'Horas de estudio':'i1','Calificacion de examen anterior':'i2','Calificacion de examen futuro':'d'})
df['i2']=df['i2']/10
df['d']=df['d']/10

df['i1d']=df['i1']*df['d']
df['i1²']=df['i1']**2
df['i2d']=df['i2']*df['d']
df['i2²']=df['i2']**2
df['i1i2']=df['i1']*df['i2']

Si1=df['i1'].sum()
Si2=df['i2'].sum()
Sd=df['d'].sum()
Si1d=df['i1d'].sum()
Si1i1=df['i1²'].sum()
Si2d=df['i2d'].sum()
Si2i2=df['i2²'].sum()
Si1i2=df['i1i2'].sum()
print(df)

###################################################################################################
valores = np.array([ [Si1, Si2,len(df)],[Si1i1, Si1i2, Si1],[Si1i2, Si2i2, Si2] ])
resultados = np.array([Sd, Si1d, Si2d])
solucion=np.linalg.solve(valores,resultados)
print(f'ax,bz,c:{solucion}')
print('Proyección')
x=int(input("Horas de estudio: "))
z=int(input("Última calificación: "))
a=(x*solucion[0])+(z*solucion[1])+solucion[2]
print("Próxima calificación: ",a)
###################################################################################################
centros_horas=np.array([[3,6.5],[5.6,8],[8.5,9]])
centros_calificaciones=np.array([[6,6],[7.5,7.5],[9,9]])
media_x_horas = df['i1'].mean()
media_x_calificacion = df['i2'].mean()
media_y = df['d'].mean()
#############Figura 1
fig, ax=plt.subplots()
ax.scatter(df['i1'], df['d'], color='blue', label='Datos')
for centro in centros_horas:
    circle=plt.Circle((centro[0],centro[1]), 1.5, color='red', fill=False, linestyle='-')
    ax.add_artist(circle)
ax.scatter(centros_horas[:,0], centros_horas[:,1], color='red', marker='X')
plt.axvline(media_x_horas, color='gray', linestyle='--', label=f'Media X = {media_x_horas:.2f}')
plt.axhline(media_y, color='gray', linestyle='--', label=f'Media Y = {media_y:.2f}')
ax.set_xlabel('Horas de estudio')
ax.set_ylabel('Proxima calificaciones')
ax.legend(loc='upper left')
ax.set_title('Horas de estudio x Calificaciones futuras')
#ax.set_xlim(0,10)
#ax.set_xlim(0,10)
plt.grid(True)
plt.show()
############# Figura 2
fig, ax=plt.subplots()
ax.scatter(df['i2'], df['d'], color='blue', label='Datos')
for centro in centros_calificaciones:
    circle=plt.Circle((centro[0],centro[1]), 1, color='red', fill=False, linestyle='-')
    ax.add_artist(circle)
ax.scatter(centros_calificaciones[:,0], centros_calificaciones[:,1], color='red', marker='X')
plt.axvline(media_x_calificacion, color='gray', linestyle='--', label=f'Media X = {media_x_horas:.2f}')
plt.axhline(media_y, color='gray', linestyle='--', label=f'Media Y = {media_y:.2f}')
ax.set_xlabel('Última calificación')
ax.set_ylabel('Proxima calificación')
ax.legend(loc='upper left')
ax.set_title('Última calificación x Próxima calificación')
#ax.set_xlim(0,10)
#ax.set_xlim(0,10)
plt.grid(True)
plt.show()
"""
plt.figure(figsize=(10, 6))

plt.scatter(df['i1'], df['d'], color='blue', label='Datos')
for centro in centro:
    circle=plt.circle((centro[o],centro[1]), 5, color='red', fill=False, linestyle='--', label=Centro)
    
plt.axvline(media_x_horas, color='red', linestyle='-', label=f'Media X = {media_x_horas:.2f}')
plt.axhline(media_y, color='red', linestyle='-', label=f'Media Y = {media_y:.2f}')

plt.xlabel('Horas de Estudio')
plt.ylabel('Próxima calificación')
plt.title('Horas de Estudio X Próximaalificación')
plt.legend()

plt.grid(True)
plt.show()
"""
"""
media_x_calificacion = df['i2'].mean()
media_y = df['d'].mean()

plt.figure(figsize=(10, 6))

plt.scatter(df['i2'], df['d'], color='blue', label='Datos')

plt.axvline(media_x_calificacion, color='red', linestyle='-', label=f'Media X = {media_x_calificacion:.2f}')
plt.axhline(media_y, color='red', linestyle='-', label=f'Media Y = {media_y:.2f}')

plt.xlabel('Última calificación')
plt.ylabel('Próxima calificación')
plt.title('Última calificación X Calificación Futura')
plt.legend()

plt.grid(True)
plt.show()
"""