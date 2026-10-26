# Crear una función llamada convertir_a_segundos que reciba una cantidad de minutos y 
# devuelva el equivalente en segundos.

def convertir_a_segundos(minutos):
    return int(minutos) * 60

print(convertir_a_segundos(5))
print(convertir_a_segundos(12))

# Crear una función calcular_precio_final que reciba un precio y un porcentaje de impuesto, 
# y devuelva el precio final.

# Ejemplo: un producto cuesta $10.000 y tiene un impuesto del 21 %.

def calcular_precio_final(precio, porcentajeImpuesto):
    # calcular_precio_final(10000, 21) -> 12100
    porcentaje = 1 + (porcentajeImpuesto / 100) # 21 / 100 -> 0.21 + 1 -> 1.21
    # 1.21 * precio -> precio final
    return precio * porcentaje

print(calcular_precio_final(10000, 21))

# Crear una función llamada encontrar_menor que reciba una lista de números y 
# devuelva el menor, sin utilizar min().

lista = ["h", "o", "l", "a"]

def encontrar_menor(lista):
    menor = lista[0]
    for numero in lista:
        if menor > numero:
            menor = numero
    return menor

numeros = [18, 4, 27, 9, 12]

print(encontrar_menor(numeros))

# Crear una función contar_vocales que reciba un texto y devuelva cuántas vocales contiene. 
# Para simplificar, considerar las vocales a, e, i, o, u, 
# tanto mayúsculas como minúsculas, sin contar vocales acentuadas.

def contar_vocales(texto):
    textoMinuscula = str.lower(texto)
    cantidadVocales = 0
    for letra in textoMinuscula:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            cantidadVocales += 1
    return cantidadVocales

print(contar_vocales("Programacion"))

# Crear una función es_bisiesto(anio) que devuelva True 
# si un año es bisiesto y False en caso contrario.
# Reglas:
# - Si el año es divisible por 400, es bisiesto.
# - Si es divisible por 100, pero no por 400, no es bisiesto.
# - Si es divisible por 4, pero no por 100, es bisiesto.
# - En cualquier otro caso, no es bisiesto.

def es_bisiesto(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Crear una función determinar_ganador(jugador1, jugador2) 
# que reciba las elecciones de dos jugadores y devuelva "Jugador 1", "Jugador 2" o "Empate".

def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        return "Jugador 1"
    else:
        return "Jugador 2"

print(determinar_ganador("piedra", "tijera"))
print(determinar_ganador("papel", "tijera"))
print(determinar_ganador("piedra", "piedra"))

# Un número es perfecto cuando la suma de sus divisores positivos, 
# excluyéndose a sí mismo, es igual al número.

# Por ejemplo, \(6 = 1 + 2 + 3\).

# Crear una función es_perfecto(numero).

def es_perfecto(numero):
    if numero <= 1:
        return False
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor
    return suma == numero


print(es_perfecto(6))    # True
print(es_perfecto(28))   # True
print(es_perfecto(12))   # False