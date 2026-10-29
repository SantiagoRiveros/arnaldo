import pandas as pd

df = pd.read_csv("datos.csv")

filtro = df["categoria"] == "Accesorios"
print(filtro)
print(df[filtro])

filtro = df[df["categoria"] == "Accesorios"]
print(filtro)

# Productos con precio mayor a $100.000
print(df[df["precio"] > 100000])

# Ventas con cantidad igual a 2
print(df[df["cantidad"] == 2])

# ventas de Cordoba
print(df[df["region"] == "Cordoba"])

# productos que no sean de la categoria audio
print(df[df["categoria"] != "Audio"])

# Filtrar con varios valores con isIn.
print(
    df[df["region"].isin(["Buenos Aires", "Cordoba"])]
)

# ordenar valores con sort_values
print("--------------------------------")
# Ascendente
print(df.sort_values("precio"))
print("--------------------------------")
# descentente
print(df.sort_values("precio", ascending=False))
print("--------------------------------")
# Ordenar por mas de una columna
print(
    df.sort_values(
        ["categoria", "precio"],
        ascending=[True, False]
    )
)

# Columnas calculadas
df["total"] = df["precio"] * df["cantidad"]

df.to_csv("datos-v2.csv")

