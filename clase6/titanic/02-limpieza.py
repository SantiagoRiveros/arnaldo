import pandas as pd


df = pd.read_csv("titanic.csv")
# Valores faltantes:
print(df.isna().sum())

# Reemplazamos la edad por edad promedio:
df["Age"] = df["Age"].fillna(df["Age"].mean())

# reemplazamos embarked
df["Embarked"] = df["Embarked"].fillna("X")

# Eliminamos Cabin, passengId y Name
df = df.drop(["Cabin", "PassengerId", "Name", "Ticket"], axis=1)

# Revisamos y cambiamos el tipo de Age
df["Age"] = df["Age"].astype(int)

# Ver si tenemos duplicados:
print("Duplicados:")
print(df.duplicated().sum())

df.to_csv("titanic-v2.csv", index=False)
