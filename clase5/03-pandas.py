import pandas as pd

# Pandas es especialmente util para el uso, manejo y creacion de Dataframes
# Que es un dataframe? es una tabla con filas y columnas.
# Se llama tambien -> Dato tabular, son datos bidimensionales

datos = {
    "producto": ["Teclado", "Mouse", "Monitor", "Auriculares"],
    "precio": [25000, 12000, 150000, 35000],
    "cantidad": [2, 5, 1, 3]
}

dataframe = pd.DataFrame(datos)

print(dataframe)

# Cada clave del diccionario se convierte en columna
# Las listas contienen los valores de cada columna
# El indice identifica las filas y si no se especifica otro, empieza en 0

# head -> Muestra las primeras cinco filas por defecto
print("HEAD")
print(dataframe.head())

# shape -> Devuelve la cantidad de filas y columnas
print("SHAPE")
print(dataframe.shape)

# columns -> Devuelve los nombres de las columnas
print("COLUMNS")
print(dataframe.columns)

# dtypes -> Muestra el tipo de dato de cada columna
print("DTYPES")
print(dataframe.dtypes)

# info -> Resume la estructura y lso valores no nulos
print("INFO")
print(dataframe.info())

# describe -> resumen estadistico de las columnas numericas
print("DESCRIBE")
print(dataframe.describe())

# Count -> Conteo
# Mean -> pROMEDIO
# STD -> Desviacion estandar
# 25%, 50% y 75% -> Cuartiles