# Trabajo práctico: Introducción a NumPy

**Tema:** Arrays, operaciones y funciones con NumPy  
**Objetivo:** Practicar arrays, cálculos, condicionales, bucles y funciones utilizando NumPy.

## Instrucciones

- Resolver los ejercicios utilizando Python y NumPy.
- Crear las funciones solicitadas respetando sus parámetros.
- Utilizar `return` para devolver resultados cuando se indique.
- No utilizar Pandas.
- Probar cada función con al menos dos ejemplos diferentes.
- No utilizar `input()`.

Para comenzar, importar NumPy:

```python
import numpy as np
```

## Ejercicio 1. Crear arrays

Crear los siguientes arrays:

1. Un array con los números del 1 al 10.
2. Un array con los números pares del 2 al 20.
3. Un array de cinco ceros.
4. Un array con los números 10, 20, 30, 40 y 50.

Mostrar cada array por pantalla.

## Ejercicio 2. Operaciones matemáticas

Crear un array con los precios de cinco productos:

```python
precios = np.array([1500, 2300, 1800, 3200, 2500])
```

Resolver:

1. Aumentar todos los precios un 10 %.
2. Calcular los precios con un descuento de $500 por producto.
3. Mostrar el precio más alto.
4. Mostrar el precio más bajo.
5. Calcular el precio promedio.

## Ejercicio 3. Analizar notas

Crear el siguiente array:

```python
notas = np.array([8, 5, 10, 4, 7, 6, 3, 9])
```

Resolver:

1. Mostrar todas las notas.
2. Calcular el promedio.
3. Mostrar la nota máxima y la mínima.
4. Crear un nuevo array que contenga solamente las notas mayores o iguales a 6.
5. Contar cuántos alumnos aprobaron.
6. Contar cuántos alumnos desaprobaron, considerando que se aprueba con una nota igual o superior a 6.

## Ejercicio 4. Filtrar temperaturas

Crear el siguiente array:

```python
temperaturas = np.array([18, 25, 31, 16, 28, 34, 22, 19, 30])
```

Resolver:

1. Mostrar las temperaturas superiores a 25 grados.
2. Mostrar las temperaturas inferiores a 20 grados.
3. Crear un array con las temperaturas entre 20 y 30 grados, inclusive.
4. Contar cuántas temperaturas superan los 30 grados.

## Ejercicio 5. Función para calcular el promedio

Crear una función llamada `calcular_promedio` que reciba un array de números y devuelva su promedio.

Ejemplo:

```python
numeros = np.array([10, 8, 6, 9, 7])

resultado = calcular_promedio(numeros)

print(resultado)  # 8.0
```

Probar la función con dos arrays diferentes.

## Ejercicio 6. Función para contar aprobados

Crear una función llamada `contar_aprobados` que reciba un array de notas y devuelva la cantidad de notas mayores o iguales a 6.

Ejemplo:

```python
notas = np.array([4, 7, 8, 3, 10, 6])

print(contar_aprobados(notas))  # 4
```

Resolverlo utilizando un bucle `for` y un contador. No utilizar todavía `np.sum()` para contar.

## Ejercicio 7. Función para obtener números pares

Crear una función llamada `obtener_pares` que reciba un array de números y devuelva un nuevo array con los números pares.

Ejemplo:

```python
numeros = np.array([3, 8, 12, 5, 7, 10, 15, 20])

print(obtener_pares(numeros))
# [ 8 12 10 20]
```

Resolverlo utilizando un bucle y una lista auxiliar. Al finalizar, convertir la lista en un array de NumPy.

## Ejercicio 8. Analizar ventas

Una tienda registró las siguientes ventas diarias:

```python
ventas = np.array([12000, 8500, 15000, 7000, 18000, 9500, 22000])
```

Resolver:

1. Calcular la facturación total.
2. Calcular la venta promedio.
3. Mostrar las ventas superiores al promedio.
4. Contar los días con ventas superiores a $10.000.
5. Crear una función llamada `analizar_ventas` que reciba el array y devuelva la venta máxima.

Ejemplo:

```python
print(analizar_ventas(ventas))  # 22000
```

## Ejercicio 9. Desafío integrador

Una persona registra la cantidad de horas que estudia cada día durante una semana:

```python
horas = np.array([2, 3, 1, 4, 2, 5, 3])
```

Crear una función llamada `analizar_estudio` que reciba el array y devuelva un diccionario con:

- `"total_horas"`: suma de las horas estudiadas.
- `"promedio"`: promedio diario.
- `"maximo"`: mayor cantidad de horas estudiadas en un día.
- `"dias_intensivos"`: cantidad de días en los que estudió 3 horas o más.

Ejemplo del formato esperado:

```python
{
    "total_horas": 20,
    "promedio": 20 / 7,
    "maximo": 5,
    "dias_intensivos": 4
}
```

**Importante:** Para contar los días intensivos, utilizar un bucle `for` y un contador.

## Entrega

Entregar un archivo `.py` o un notebook de Google Colab con todos los ejercicios resueltos, ordenados y con comentarios breves que expliquen las partes principales del código.
