# Primero en los archivos importamos las bibliotecas que vamos a usar:
import numpy as np # import numpy -> trae la biblioteca. as np -> Le pone de nombre "np" a la biblioteca

# Listas de python vs Arrays de Numpy:

numeros = [10, 20, 30, 40]

print(numeros) # [10, 20, 30, 40]
print(numeros[0]) # 10
print(numeros[2]) # 30

numeros2 = np.array([10, 20, 30, 40])

print(numeros2)
print(numeros2[0])
print(numeros2[2])

# np.array convierte una secuencia de valores (lista) en un array de numpy
# Los indices empiezan en 0, igual que en las listas
# Los arrays numericos normalmente trabajan con un tipo de dato homogeneo, por ejemplo
# enteros o decimales.

# Python
numeros = [10, 20, 30]

def duplicarNumeros(lista):
    duplicados = []
    for numero in lista:
        duplicados.append(numero * 2)
    return duplicados

duplicados = duplicarNumeros(numeros)
print(duplicados)

# NUmpy 
numeros2 = np.array([10, 20, 30])

duplicados = numeros2 * 2

conAumento = numeros2 * 1.10

resta = numeros2 - 3

print(duplicados)

# Hay diferentes formas de crear arrays de numpy:

array1 = np.arange(1,11)
array2 = np.zeros(5)
array3 = np.ones(4)
array4 = np.arange(0, 21, 5)

print(array1)
print(array2)
print(array3)
print(array4)