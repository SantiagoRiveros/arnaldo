def duplicar(numero):
    return numero * 2

print(duplicar(5)) # numero * 2 =  10
print(duplicar(10)) # 20
print(duplicar(3)) # 6

def sumar(a, b):
    return a + b

print(sumar(3, 7)) #  10
print(sumar(10, 5)) # 15
print(sumar(100, 20)) # 120

def presentar(nombre, edad):
    return nombre + " tiene " + str(edad) + " años"

print(presentar("Lucía", 25))
print(presentar("Marcos", 30))

print(presentar(25, "Lucía"))