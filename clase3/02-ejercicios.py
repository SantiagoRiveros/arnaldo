# Ejercicio 1 — Cuenta regresiva
# Utilizar un ciclo para mostrar los números del 10 al 1 y, al terminar, imprimir "¡Despegue!".

contador = 10

while contador >= 1:
    if contador == 1:
            print("Contador:", contador)
            print("Despegue!")
    else:
          print("Contador:", contador)
    contador -= 1

# Ejercicio 2 — Tabla de multiplicar
# Crear una variable numero = 7 y mostrar su tabla de multiplicar desde el 1 hasta el 10 usando for.

for numero in range(1, 11):
      print("7 x", numero)
      print(7 * numero)


# Ejercicio 3 — Suma de números
# Utilizar un ciclo para sumar todos los números del 1 al 100 y mostrar el resultado final.
acumulador = 0

for numero in range(1, 101):
      acumulador += numero

print(acumulador)

# Ejercicio 4 — Números pares
# Mostrar todos los números pares del 2 al 20 usando un ciclo.

for numero in range(2, 21, 2):
      print(numero)


""" 
Ejercicio 5 — Análisis de valores
Dada esta lista:
numeros = [4, 9, 2, 15, 8, 3, 12]

Recorrerla con for y mostrar cada número mayor que 7. Para este ejercicio, explicale previamente que una lista permite almacenar varios valores.
 """
numeros = [4, 9, 2, 15, 8, 3, 12]

for numero in numeros:
      if numero > 7:
            print(numero)

""" 
Ejercicio 3. Potencias

Dado el número 2, mostrar sus primeras 8 potencias, desde \(2^1\) hasta \(2^8\).

El resultado debería mostrar 2, 4, 8, 16 y así sucesivamente.
"""

potencia = 1

while potencia <= 8:
      print(2 ** potencia)
      potencia += 1

""" 
Ejercicio 5. Suma de números impares

Calcular la suma de todos los números impares entre 1 y 99. Mostrar únicamente el resultado final.
"""

acumulador = 0
for numero in range(1, 100, 2):
      print(numero)
      acumulador += numero

print(acumulador)

""" 
Ejercicio 6. Contar números divisibles

Recorrer los números del 1 al 100 y contar cuántos son divisibles por 7. Mostrar la cantidad total.
"""

contador = 0

for numero in range(1, 101):
      if numero % 7 == 0:
            contador += 1

print("contador:", contador)