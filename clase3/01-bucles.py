# Bucles / Loops / Ciclos son estructuras de control, que sirven para repetir instrucciones.

# Ciclo while
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1

# Ciclo for y range()
# El ciclo for permite recorrer uuna secuencia de valores, para empezar a usarlo empezemos con range.

# range(1,6) e sel rango entre estos numeros, sin incluir el ultimo 
for numero in range(1, 6):
    print("for range")
    print(numero)

# numero es cada uno de los elementos dentro del rango provisto

for numero in range(2, 11, 2):
    print(numero)
# El ultimo elemento en el range, osea el tercero, es el "Step" que toma entre uno y el otro

frutas = ["Kiwi", "Pera", "Manzana", "frutilla"]

for fruta in frutas:
    print(fruta)

# Contadores y acumuladores