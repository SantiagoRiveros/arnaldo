# Ej 1 -Crear un programa que tenga una variable 
# numero y muestre si el número es positivo, negativo o igual a cero.

numero = 8

if numero > 0:  
    print("Numero positivo")
elif numero < 0:
    print("Numero Negativo")
elif numero == 0:
    print("Cero")

""" 
Una tienda ofrece un descuento del 15 % cuando la compra alcanza los $50.000.

Crear un programa que:
- Guarde el importe de la compra en una variable.
- Si alcanza los $50.000, aplique el descuento.
- En caso contrario, mantenga el importe original.
- Muestre el total a pagar.
"""

importe_compra = 55000

if importe_compra >= 50000:
    importe_compra = importe_compra * 0.85

print("Importe a pagar:", importe_compra)