# Vamos a usar matplotlib que es una libreria que nos facilita
# la visualizacion de datos

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# Tipos de graficos:

# Grafico de barras:
# Comparar categorias

sobrevivientes = df["Survived"].value_counts().sort_index()

"""  
Sintaxis basica:

plt.tipo_de_grafico(datos)

plt.title("Título")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()
"""

# bar = grafico de barras
plt.bar(["No sobrevivio", "Sobrevivio"], sobrevivientes.values)

# title = Es el titulo
plt.title("Supervivencia en el titanic")
# x label = subtitulo del eje x (Horizontal)
plt.xlabel("Estado")

# y label = Subtitutlo del eje y (vertical)
plt.ylabel("Cantidad de pasajeros")

# Esto lo guarda como archivop
plt.savefig("barras.jpg")
# Esto muestra el grafico
plt.show()

# Esto borra el cache temporal del grafico
plt.clf()

# Grafico de torta:
# Mostrar que porcentaje representa cada categoria sobre el total:
plt.pie(
    df["Survived"].value_counts(),
    labels=["No sobrevivieron", "Sobrevivieron"],
    autopct="%1.1f%%"
)

plt.title("Supervivencia en el titanic")
plt.savefig("torta.jpg")
plt.show()
plt.clf()

# Histograma:
# # MOstrar comos e distribuyen los valores numericos:
plt.hist(df["Age"], bins=10) # Frecuencia de muestreo:

plt.title("Distribucion por edades")
plt.xlabel("Edad")
plt.ylabel("Cantidad de pasajeros")
plt.savefig("histograma2.jpg")
plt.show()
plt.clf()

# Grafico de lineas
# Mostrar como varia una cantidad a lo largo de un orden o secuencia

plt.plot(
    df["Age"].value_counts().sort_index().index,
    df["Age"].value_counts().sort_index().values
)

plt.title("Pasajeros segun edad")

plt.xlabel("Edad")
plt.ylabel("Cantidad de pasajeros")
plt.savefig("lineas.jpg")
plt.show()
plt.clf()

# Grafico de dispersion (Scatter)
# Observar la relacion entre dos variables numericas.

plt.scatter(df["Age"], df["Fare"])

plt.title("Edad y precio del pasaje")
plt.xlabel("Edad")
plt.ylabel("Precio del pasaje")
plt.savefig("scatter.jpg")
plt.show()
plt.clf()

# Diagrama de caja (Boxplot)
plt.boxplot(df["Fare"])

plt.title("Distribucion de precios")
plt.ylabel("Precio del pasaje")
plt.savefig("boxplot.jpg")
plt.show()
plt.clf()

# Heatmap
# Correlacion entre variables numericas
plt.imshow(df.corr(numeric_only=True), cmap="coolwarm")

plt.colorbar()

plt.title("Correlación entre variables del Titanic")
plt.xticks(range(len(df.corr(numeric_only=True).columns)), df.corr(numeric_only=True).columns, rotation=45)
plt.yticks(range(len(df.corr(numeric_only=True).columns)), df.corr(numeric_only=True).columns)

plt.show()