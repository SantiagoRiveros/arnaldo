import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

# Grafico de barras
# Sirve para comparar cantidades entre catergorias:

# Cantidad de estudiantes por genero.


plt.bar(
        df["gender"].value_counts().index, # Eje x
        df["gender"].value_counts().values # Eje Y
        )

plt.title("Cantidad de estudiantes por genero")
plt.xlabel("Genero")
plt.ylabel("Cantidad")
plt.savefig("estudiantes-por-genero.jpg")

plt.clf()

# Hay mas estudiantes hombres o mujeres? -> Mujeres

# Grafico circular (pie / torta)

# Muestra proporciones o porcentajes

# Estudiantes que completaron el curso

plt.pie(
    df["test preparation course"].value_counts(), # Seleccionamos la columan a analizar
    labels=df["test preparation course"].value_counts().index, # Indica que nombres queremos mostrar ocmo etiquetas en cada porcion del grafico
    autopct="%1.1f%%" # Esta opcion permite mostrar automaticamente los porcentajes dentro de cada porcion del grafico
    ) 
"""  
% indica que vamos a mostrar un porcentaje
1 espacio minimop para el numero entero
.1 un decimal de precision
f formato numerico decimal
%% Imprime el simbolo %

Ejemplo: 66.6%
"""

plt.title("Preparacion para el examen")

plt.savefig("preparacion-examen.jpg")

plt.clf()

# Histograma

# Sirve para observar como se distribuyen los valores

# Distribucion de las notas de matematica, lectura y escritura

# De matematica
plt.hist(df["math score"], bins=10)

plt.title("Distribucion de notas en matematica")

plt.xlabel("Nota")
plt.ylabel("Cantidad de estudiantes")

plt.savefig("distribucion-notas-matematica.jpg")

plt.clf()

# De lectura
plt.hist(df["reading score"], bins=10)

plt.title("Distribucion de notas en lectura")

plt.xlabel("Nota")
plt.ylabel("Cantidad de estudiantes")

plt.savefig("distribucion-notas-lectura.jpg")

plt.clf()

# De escritura
plt.hist(df["writing score"], bins=10)

plt.title("Distribucion de notas en escritura")

plt.xlabel("Nota")
plt.ylabel("Cantidad de estudiantes")

plt.savefig("distribucion-notas-escritura.jpg")

plt.clf()

# Grafico de lineas

# Sirve para mostrar variaciones siguiendo un orden, muchas veces
# A lo largo del tiempo

# Como no tenemos fechas, vamos a usar las 3 materias para comparar sus promedios

plt.plot(
    ["Matematica", "Lectura", "Escritura"], # Eje X
    [
        df["math score"].mean(), # Ejes y
        df["reading score"].mean(),
        df["writing score"].mean()
    ],
    marker="o" # Indica que queremos mostrar un "o" en cada punto de la linea
)

plt.title("Promedio de notas por materia")
plt.xlabel("Materia")
plt.ylabel("Promedio")

plt.savefig("promedio-notas.jpg")

plt.clf()

# Diagrama de caja boxplot

# Sirve para ve rla distribucion, mediana y outliers

# Comprar las notas de las tres materias:
plt.boxplot([
    df["math score"], # las cajas
    df["reading score"],
    df["writing score"]
])

plt.title("Distribucion de notas por materia")

plt.xticks( # Permite modificar las etiquetas que aparecen en el eje x
    [1, 2, 3], # Indica las posiciones
    ["Matematica", "Lectura", "Escritura"] # Indica los titulos
)

plt.ylabel("Nota")

plt.savefig("distribucion-notas-materia.jpg")

plt.clf()
# Mapa de calor

# Sirve para representar valores mediante colores y detectar
# relaciones entre variables

# Tenemos dos tipos de relaciones: positiva y negativa

# positiva es 1 negativa es -1 cuanto mas cerca del 0, menos correlacion tienen

# positiva es que variable A sube 1 y variable B sube 1
# negativa, es variable A sube, B baja, o al re ves

# Correlacion entre las notas

correlacion = df[
    ["math score", "reading score", "writing score"]
].corr()

plt.figure(figsize=(9, 7))

plt.imshow(
    correlacion,
    cmap="RdYlBu_r",
    vmin=-1,
    vmax=1
)

# Barra de colores
plt.colorbar(label="Coeficiente de correlación", shrink=0.8)

# Etiquetas de los ejes
nombres = ["Matemática", "Lectura", "Escritura"]

plt.xticks(range(3), nombres)
plt.yticks(range(3), nombres)

# Mostrar los valores dentro de las celdas
for i in range(3):
    for j in range(3):

        valor = correlacion.iloc[i, j]

        plt.text(
            j, i,
            f"{valor:.2f}",
            ha="center",
            va="center",
            fontsize=16,
            fontweight="bold",
            color="black"
        )

plt.title("Correlación entre materias", fontsize=16, pad=20)

plt.tight_layout()

plt.savefig("correlaciones-notas.jpg")