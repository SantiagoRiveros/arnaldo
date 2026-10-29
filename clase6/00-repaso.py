import pandas as pd

datos = {
    "producto": [
        "Teclado", "Mouse", "Monitor", "Auriculares",
        "Notebook", "Mouse", "Teclado", "Monitor"
    ],
    "categoria": [
        "Accesorios", "Accesorios", "Pantallas", "Audio",
        "Computadoras", "Accesorios", "Accesorios", "Pantallas"
    ],
    "precio": [
        25000, 12000, 150000, 35000,
        850000, 12000, 25000, 150000
    ],
    "cantidad": [2, 5, 1, 3, 1, 8, 4, 2],
    "region": [
        "Buenos Aires", "Córdoba", "Buenos Aires", "Mendoza",
        "Córdoba", "Buenos Aires", "Mendoza", "Córdoba"
    ]
}

dataframe = pd.DataFrame(datos)

# dataframe.to_csv("datos.csv", index=False)

# Seleccionar una sola columna

print(dataframe["producto"])

# Si yo quiero varias columnas

print(dataframe[["producto", "precio"]])

# Seleccionar filas:

# iloc selecciona por posicion

print(dataframe.iloc[1])
print(dataframe.iloc[2])
print(dataframe.iloc[3])

# Seleccionar varias filas:
print(dataframe.iloc[0:3])
# Devuelve las filas de las posiciones 0, 1, y 2, el limite final no se incluye

# Seleccionar filas y columnas
print(dataframe.iloc[0:3, 0:2]) # selecciona primeras 3 filas, y 2 columnas

# loc: seleccionar por etiquetas
# con Loc seleccionamos utilizando las etiquetas del indice y los nombres de las columnas

print(dataframe.loc[0])
print(dataframe.loc[0, "producto"])