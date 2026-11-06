import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("penguins_size.csv")

sns.set_style("whitegrid")

# sns.set_palette("Set2")

# Grafico de dispersion:

# Largo y profundidad del pico.

sns.scatterplot(
    data=df,
    x="culmen_length_mm",
    y="culmen_depth_mm",
    hue="species"
)

plt.title("Relacion entre largo y profundidad del pico")
plt.xlabel("Largo del pico")
plt.ylabel("Profunidad del pico")

plt.savefig("scatter.jpg")
plt.clf()

# Grafico de barras:

# Peso promedio de cada specie
sns.barplot(
    data=df,
    x="species",
    y="body_mass_g"
)

plt.title("Peso promedio por especie")
plt.xlabel("Especie")
plt.ylabel("Peso en gramos")
plt.savefig("barras.jpg")

plt.clf()
# Distribucion del peso de los pinguinos

# Histograma

sns.histplot(
    data=df,
    x="body_mass_g",
    hue="species",
    bins=15
)

plt.title("Distribucion del peso")

plt.savefig("histograma.jpg")

plt.clf()

# Boxplot:

sns.boxplot(
    data=df,
    x="species",
    y="body_mass_g"
)

plt.title("Distribucion del peso por especie")
plt.savefig("boxplot.jpg")

plt.clf()

# Violinplot

sns.violinplot(
    data=df,
    x="species",
    y="body_mass_g"
)

plt.title("Distribucion del peso por especie")
plt.savefig("violinplot.jpg")

plt.clf()
# Grafico de conteo
# Cuenta automaticamente cuantos registros hay en cada categoria

sns.countplot(
    data=df,
    x="species"
)

plt.title("Cantidad de pinguinos por especie")
plt.savefig("countplot.jpg")

plt.clf()

# Heatmap
""" plt.figure(figsize=(10, 6))

sns.heatmap(
    df[
        [
            "culmen_length_mm",
            "culmen_depth_mm",
            "flipper_length_mm",
            "body_mass_g"
        ]
    ].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

plt.tight_layout()

plt.title("Correlacion entre medidas")
plt.savefig("heatmap.jpg") """

plt.clf()

# Pairplot

sns.pairplot(
    df,
    hue="species"
)

plt.savefig("pairplot.jpg")

plt.clf()

# Regplot
sns.regplot(
    data=df,
    x="flipper_length_mm",
    y="body_mass_g"
)

plt.title("Relacion entre largo de aletas y peso")

plt.savefig("regplot.jpg")

plt.clf()

# kdeplot

sns.kdeplot(
    data=df,
    x="body_mass_g",
    hue="species",
    fill=True
)

plt.title("Distribución del peso por especie")

plt.savefig("kdeplot.jpg")

plt.clf()

#permite identificar dónde se concentran los valores y comparar las distribuciones de las especies.

# swarmplot

sns.swarmplot(
    data=df,
    x="species",
    y="body_mass_g",
    hue="species"
)

plt.title("Peso de cada pingüino según su especie")

plt.savefig("swarmplot.jpg")