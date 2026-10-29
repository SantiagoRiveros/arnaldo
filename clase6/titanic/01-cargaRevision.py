import pandas as pd

titanic = pd.read_csv("titanic.csv")

# primeras 5 filas
print(titanic.head())

print("----------------------------")
print("Dimensiones:")
print(titanic.shape)

print("----------------------------")

print("Tipos de datos:")
print(titanic.dtypes)

print("----------------------------")

print("Informacion general:")
print(titanic.info())

print("----------------------------")

print("Estadisticas:")
print(titanic.describe())