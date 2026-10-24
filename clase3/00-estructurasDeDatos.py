# Listas y Diccionarios.

# Queremos guardar las frutas que vende una verduleria

fruta1 = "Pera"
fruta2 = "Manzana"
fruta3 = "frutilla"
fruta4 = "sandia"

# El problema es que no es escalable, no es incremental.
# cuando tenes que agregar o sacar algo, es un problema.

# Listas:
# Son datos unidimensionales, que sirven para guardar multiples datos en una variable.

frutas = ["Pera", "Manzana", "Frutilla", "Sandia"]
# Los datos dentro de la lista, se diferencian y separan usando comas
# La posicion de los elementos esta bien definida.
# Estas posiciones se llaman INDICES (index).
# Como cuento los indices?

personas = ["Yamila", "Lucias", "Roman", "Lorena", "Fabricio"]
# Indices      0          1         2       3          4

print(personas[3])

frutasBidimesionales = [
    ["Pera", "Kiwi"],
    ["Naranja", "Mango"]
]

alumnos = [
    ["Ernesto", "Fabian"],
    ["Carlos", "Ramon"]
]

# Como accedemos a un elemento?
# Sintaxis: nombreLista[numeroIndice]

string = ["H", "o", "l", "a", " ", "M", "u", "n", "d", "o"]

# Diccionarios:
# Son otra estructura de datos, primero veamos que soluciona

# Quiero guardar los datos de un usuario:

nombre = "Carlos"
apellido = "Tevez"
profesion = "Futbolista"
edad = 42

# Es dificil relacionar los datos
# Los diccionarios se caracterizan por tener pares de clave-valor
usuario = {
    nombre:  "Carlos",
    apellido: "Tevez",
    profesion: "Futbolista",
    edad: 42
}

""" 
sintaxis:
nombreDiccionario = {
    clave1: valor1,
    clave2: valor2
}
"""

# Como accedo a los elementos que lo conforman?
# sintaxis: nombreDiccionario["nombreClave"]

print(usuario["profesion"])
print(usuario)

# Tupla:
# Es IGUAL a la lista, pero sus valores no pueden ser modificados:
tuplaNumeros = (1, 2, 3, 4, 5, 6, 7)

# porque lo usarias?
# dos principales motivos:

# Seguridad: Al ser inmutable, tus datos estan seguros
# Eficiencia: Ocupa menos espacio interno, por ende es mas rapido, ideal para calculo.

