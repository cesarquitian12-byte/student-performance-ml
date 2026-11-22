
import pandas as pd

# Cargar el dataset
ruta = "data/raw/student-mat.csv"
df = pd.read_csv(ruta, sep=";")

print("\n===== EXPLORACION DEL DATASET =====")

print("\nPrimeros 5 estudiantes:")
print(df.head())

print("\nDimensiones del dataset:")
print(df.shape)

print("\nVariables disponibles:")
print(df.columns.tolist())

print("\nInformacion general:")
df.info()

print("\nValores faltantes:")
print(df.isnull().sum())

print("\nRegistros duplicados:")
print(df.duplicated().sum())

print("\nEstadisticas de calificaciones:")
print(df[["G1", "G2", "G3"]].describe())


# 8. Crear la variable de riesgo academico

df["riesgo_academico"] = (df["G3"] < 10).astype(int)

# 9. Contar estudiantes por categoria

print("\n===== DISTRIBUCION DEL RIESGO ACADEMICO =====")

conteo = df["riesgo_academico"].value_counts()

print("Sin riesgo (0):", conteo.get(0, 0))
print("Con riesgo (1):", conteo.get(1, 0))

# 10. Calcular porcentajes

porcentajes = (
    df["riesgo_academico"]
    .value_counts(normalize=True) * 100
)

print("\nPorcentajes:")
print(porcentajes.round(2))

# 11. Resumen de la calificacion final

print("\n===== RESUMEN DE G3 =====")
print(df["G3"].describe())

# 12. Correlacion entre calificaciones

print("\n===== CORRELACION DE CALIFICACIONES =====")

print(df[["G1", "G2", "G3"]].corr().round(3))


import matplotlib.pyplot as plt
import seaborn as sns

# Visualizar distribucion de calificaciones

plt.figure(figsize=(10, 5))

sns.histplot(
    data=df,
    x="G3",
    bins=20,
    kde=True
)

plt.title("Distribucion de las calificaciones finales")
plt.xlabel("Calificacion final (G3)")
plt.ylabel("Numero de estudiantes")

plt.tight_layout()
plt.show()

# Visualizar distribucion del riesgo

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="riesgo_academico"
)

plt.title("Distribucion del riesgo academico")
plt.xlabel("Riesgo academico (0 = No, 1 = Si)")
plt.ylabel("Numero de estudiantes")

plt.tight_layout()
plt.show()


# 13. Frecuencia exacta de cada calificacion final

print("\n===== FRECUENCIA DE CALIFICACIONES G3 =====")
print(df["G3"].value_counts().sort_index())

# 14. Identificar estudiantes con calificacion cero

print("\n===== ESTUDIANTES CON G3 IGUAL A CERO =====")

estudiantes_cero = df[df["G3"] == 0]

print("Cantidad:", len(estudiantes_cero))

print(estudiantes_cero[
    ["age", "studytime", "failures", "absences", "G1", "G2", "G3"]
].head(10))

# 15. Revisar valores extremos mediante cuartiles

Q1 = df["G3"].quantile(0.25)
Q3 = df["G3"].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print("\n===== REVISION DE VALORES EXTREMOS =====")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Limite inferior:", limite_inferior)
print("Limite superior:", limite_superior)

print(
    "Valores fuera de los limites:",
    ((df["G3"] < limite_inferior) |
     (df["G3"] > limite_superior)).sum()
)
