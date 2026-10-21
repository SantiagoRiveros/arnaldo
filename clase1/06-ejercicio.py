""" 
Consigna
Una tienda vende remeras a $12.000 cada una y pantalones a $25.000 cada uno.

Crear un programa en Python que:
1. Guarde en variables el precio de cada producto.
2. Guarde la cantidad de remeras y pantalones que se compraron.
3. Calcule el subtotal de cada producto.
4. Calcule el total de la compra.
5. Muestre por pantalla los precios, las cantidades y el total a pagar.
"""

remeras_precio = 12000
pantalones_precio = 25000

remerasCompradas = 43
pantalonesComprados = 21

subtototal_remeras = remerasCompradas * remeras_precio
subtotal_pantalones = pantalonesComprados * pantalones_precio

total = subtotal_pantalones + subtototal_remeras

print("Precio de las remeras: $", remeras_precio)
print("Precio de los pantalones: $", pantalones_precio)

print("Cantidad de remeras compradas: ", remerasCompradas)
print("Cantidad de pantalones comprados: ", pantalonesComprados)

print("Subtotal remeras: $", subtototal_remeras, ", subtotal pantalones: $", subtotal_pantalones)

print("Total a pagar: $", total)
print("Gracias por su compra!")