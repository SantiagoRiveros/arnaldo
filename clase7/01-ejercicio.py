import pandas as pd

df = pd.read_csv("titanic.csv")
# Cosas que ya sabemos hacer:
# Cuantas mujeres habia:
print(df[df["Sex"] == "female"].count())

# Para saber cuantos hombres habia:
print(df[df["Sex"] == "male"].count())

# Pero que pasa si queremos conocer el promedio de edad de cada sexo o cuantos pasajeros
# sobrevivieron segun su clase?

# Para eso usamos groupby()

# Permite agrupar registros que comparten un mismo valor y realizar operaciones sobre cvada grupo.

# La idea es:
# 1. Dividir los datos en grupos
# 2. Aplicar una operacion a cada grupo
# 3. Combinar los resultados:

# Ejemplo 1 : cantidad de pasajeros por sexo:
print("Pasajeros por sexo")
print(df.groupby("Sex")["Survived"].count())

# Otra forma de hacer esto:
print(df["Sex"].value_counts())

# Ejemplo 2 : Promedio de edad por sexo:
print("Promedio de edad por sexo")
print(df.groupby("Sex")["Age"].mean())

# Ejemplo 3 : supervivencia por clase:
print("supervivencia por clase")
print(round(df.groupby("Pclass")["Survived"].mean() * 100, 2) )

# Como survived contiene 0 y 1, calcular su promedio equivale a calcular la proporcion
# de pasajeros que sobrevivieron

# Ejemplo 4: Agrupar por mas de una columna:
print("Agrupar por mas de una columna")
print(round(df.groupby(["Sex", "Pclass"])["Survived"].mean() * 100, 2))

# Ejemplo 5 : Varias estadisticas al mismo tiempo:
print("Varias estadisticas al mismo tiempo")
print(df.groupby("Pclass")["Age"].agg(["mean", "min", "max", "count"]))

print(df.groupby("Pclass").agg({
    "Age": ["mean", "min", "max"],
    "Survived": ["mean", "sum", "count"],
    "Fare": ["mean", "max"]
}))

# Ejemplo 6 : Tablas de frecuencias cruzadas:
print(pd.crosstab(df["Sex"], df["Survived"]))

# Q1, Q2, Q3.. y Q4?
# Hablamos de cuatro partes, pero existen 3 puntos de corte: Q1, Q2 y Q3, El cuarto cuartil
# Existe, pero no se representa como Q4, por Q4 coincide con el valor maximo del conjunto de datos
# Percentil 100.
#Q1 (25%): el 25% de los datos está por debajo de este valor.
#Q2 (50%): es la mediana. El 50% está por debajo.
#Q3 (75%): el 75% está por debajo.
#Q4 (100%): sería el límite superior, es decir, el valor máximo.
# Si, tenes cuatro cuartiles, pero pero solamente 3 cuartiles que funcionan como punto de corte.

# Es como dividir una pizza en cuatro porciones, necesitas 3 cortes para obtener 4 piezas