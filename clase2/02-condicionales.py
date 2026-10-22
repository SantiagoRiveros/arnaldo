# if y else
# Un condicional permite ejecutar diferentes instrucciones dependiendo de si una condicion cumple o no

edad = 13

if edad >= 18:
    print("Es mayor de edad") # El espacio se llama identacion
else:
    print("Es menor de edad")

if edad >= 18 and edad < 65:
    print("Esta en edad laboral")
else:
    print("No esta en edad laboral")


# if: evalua una condicion
# edad >= 18: expresion que puede ser verdera o falsa
# : indica el inicio del bloque
# La indentancion señala que  isntrucciones pertenecen al bloque
# else: define que sucede si la condicion es falsa

# elif:

nota = 8

if nota >= 9:
    if nota == 10:
        print("Perfecta")
    else:
        print("Excelente")
elif nota >= 6:
    print("Aprobado")
elif nota == 4:
    print("Apenas aprobado")
else:
    print("Desaprobado")

# Cadena de condicionales
# maximo 1 if
# el if, siempre va primero, nunca puede ir otro como primera opcion
# No es obligatorio usar else o elif.
# si se agrega un else, SIEMPRE tiene que ser la ultima opcion
# El elif, puede concatenarse de manera indefinida

edad2 = 22
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puede ingresar")
else:
    print("No puede ingresar")