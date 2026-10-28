# Los 5 conceptos a memorizar:
# Una funcion es un bloque de codigo reutilizable que podemos ejecutar cuando lo necesitamos

# La estructura basica es:
""" 
def nombre_funcion(parametros):
    instrucciones
    return resultado
"""

# def -> definir funcion, le indica a python que estamos creando una funcion
# nombre -> Identificar, es el nombre que usamos para llamar a la funcion
# parametros -> Recibir datos, Son los valores que la funcion necesita para trabajar
# Indentacion -> Agrupar instrucciones, el codigo identado pertenece al cuerpo de la funcion
# return -> Devolver un resultado, permite guaradar el resultado mostrarlo despues o utilizarlo en calculo

def sumar(a, b):
    resultado = a + b
    return resultado # sumar(10, 5) = 15

total = sumar(10, 5)

# sumar(2, 2) = 4

print(total)

# def sumar(a, b) -> define la funcion y sus parametros
# a y b -> reciben los valores que le pasamos
# resultado = a + b -> Realiza el calculo
# return resultado -> Devuelve el valro calculado
# sumar(10, 5) -> llama a la funcion con los argumentos 10 y 5
# total -> Guarda el valor devuelto, que es 15

# DIferencia entre return y print

def sumar_a(a, b):
    print(a + b)

def sumar_b(a, b):
    return a + b

# La primera funcion muestra el resultado en pantalla, pero no lo devuelve como valor de retorno
# La segunda devuelve el resultado para poder re utilizarlo

resultado = sumar_a(3, 4)

print(resultado)

# Porque? porque sumar_a() muestra 7 pero no tiene un return especifico, asi que python devuelve None