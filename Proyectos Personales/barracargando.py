import time
from tqdm import tqdm

# Define el número de pasos y el tiempo total
steps = 100
time_total = 5  # en segundos

# Calcula el tiempo de espera por cada paso
time_per_step = time_total / steps

# Muestra la barra de carga
numero=int(input("Piensa en un número y escríbelo aquí: "))

for _ in tqdm(range(steps), desc="Leyendo tu mente:", unit="paso"):
    time.sleep(time_per_step)

print("Pensaste en el número ",numero)
