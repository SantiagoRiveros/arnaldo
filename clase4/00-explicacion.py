precio_a = 1500
cantidad_a = 3
total_a = precio_a * cantidad_a
print(total_a)

precio_b = 2000
cantidad_b = 4
total_b = precio_b * cantidad_b
print(total_b)

# Em ambos casos, mulptiplicamos un precio por cantidad. Si necesitamos realizar esta operacion
# muchas veces, podemos escribir una funcion y reutilizarla.

# La idea es sque una funcion agrupa instrucciones que realizan una tarea en concreto
# Podemos llamarla cada vez que necesitemos ejecutar esa tarea, sin tener que repetir logica.

# Vamos a crear nuestra primera funcion
""" 
sintaxis:
def nombreFuncion(parametro1, parametro2...):
    return
 """

# Vamos a hacer una funciomn que salude
# Las funciones tienen 2 estadios, la definicion/declaracion y la ejecucion

# Vamos a declararla:
def saludar():
    print("Hola, bienvenido a Python")

# La ejecutamos 3 veces:

saludar()
saludar()
saludar()

""" 
def indica que estamos definiendo una funcion
saludar es el nombre de la funcion
() contiene los parametros, si los hay
: indica el comienzo del bloque de la funcion
La indentacion define las instrucciones que forman parte de ella
saludar() ejecuta la funcion
 """

# funciones con parametros:
# Los parametros permiten que una funcion reciba informacion para trabajar

def suma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print(suma(3, 4))

def calculadora(numero1 = 0, numero2 = 0, operacion = ""):
    if operacion == "":
        return
    elif operacion == "suma":
        return numero1 + numero2
    elif operacion == "resta":
        return numero1 - numero2
    elif operacion == "multiplicacion":
        return numero1 * numero2
    elif operacion == "division":
        return numero1 / numero2

print(calculadora(19, 2, "suma"))

""" 
Ejercicio 3 — Análisis de palabras

Dada la siguiente lista:

palabras = ["python", "programacion", "sol", "algoritmo", "codigo", "computadora"]

Crear un programa que:

Recorra todas las palabras.

Muestre las palabras que tengan más de 6 caracteres.

Cuente cuántas palabras tienen 6 caracteres o menos.

Muestre la cantidad total de palabras analizadas.

Pista: se puede utilizar len() para conocer la longitud de una palabra.
 """

palabras = ["python", "programacion", "sol", "algoritmo", "codigo", "computadora"]

def contarPalabras(listaPalabras):
    diccionario = {
        "palabras_analizadas" : 0,
        "palabras_con6caracteres": 0
    }
    for palabra in listaPalabras:
        diccionario["palabras_analizadas"] += 1
        if len(palabra) > 6:
            diccionario["palabras_con6caracteres"] += 1
            print(palabra)
    return diccionario

print(contarPalabras(palabras))