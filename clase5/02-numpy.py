import numpy as np

ventas = np.array([12000, 15000, 9000, 18000, 16000])

print("Total:", np.sum(ventas)) # devuelve la sumatoria
print("Promedio:", np.mean(ventas)) # Devuelve promedio
print("Maximo:", np.max(ventas)) # Devuelve el maximo
print("Minimo:", np.min(ventas)) # devuelve el minimo
print("Mediana:", np.median(ventas)) # La mediana, no es lo mismo que la media.

# Filtrar valores con condiciones

# Ventas mayores a 14.000
print(ventas > 14000)
# Como se filtra realmente?
print(ventas[ventas > 14000]) # Le decis, devolveme los elementos que cumplan esta condicion

print(ventas[1]) # Lo que vos pones entre corchetes afecta el contexto del conjunto de datos
# Es decir, aca le estas diciendo que su contexto se convierta en indice = 1.

# Ventas mayores a 10.000 y menores a 15.000

print(ventas[(ventas > 10000) & (ventas < 15000)])

# cuando trabajamos con arrays, los operadores logicos cambian
# and -> &
# or -> |
# not -> !