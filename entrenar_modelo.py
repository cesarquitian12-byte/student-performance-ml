
# ==========================================
# MODELO BASELINE - STUDENT PERFORMANCE
# Clasificacion del riesgo academico
# ==========================================

import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# 1. Cargar el dataset

ruta = "data/raw/student-mat.csv"

df = pd.read_csv(ruta, sep=";")

print("\n===== ENTRENAMIENTO DEL MODELO BASELINE =====")

# 2. Crear la variable objetivo

df["riesgo_academico"] = (df["G3"] < 10).astype(int)

# 3. Separar variables predictoras y objetivo

X = df.drop(columns=["G3", "riesgo_academico"])

y = df["riesgo_academico"]

# 4. Identificar variables numericas y categoricas

variables_numericas = X.select_dtypes(
    include=["number"]
).columns.tolist()

variables_categoricas = X.select_dtypes(
    exclude=["number"]
).columns.tolist()

print("\nVariables numericas:", len(variables_numericas))
print("Variables categoricas:", len(variables_categoricas))

# 5. Dividir los datos en entrenamiento y prueba

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nRegistros de entrenamiento:", len(X_train))
print("Registros de prueba:", len(X_test))

# 6. Preparar el procesamiento de variables

preprocesamiento = ColumnTransformer(
    transformers=[
        ("numericas", StandardScaler(), variables_numericas),
        (
            "categoricas",
            OneHotEncoder(handle_unknown="ignore"),
            variables_categoricas
        )
    ]
)

# 7. Crear el modelo baseline

modelo = Pipeline(
    steps=[
        ("preprocesamiento", preprocesamiento),
        (
            "clasificador",
            LogisticRegression(max_iter=2000)
        )
    ]
)

# 8. Entrenar el modelo

modelo.fit(X_train, y_train)

print("\nModelo entrenado correctamente.")

# 9. Realizar predicciones

predicciones = modelo.predict(X_test)

# 10. Evaluar el rendimiento

accuracy = accuracy_score(y_test, predicciones)
precision = precision_score(y_test, predicciones, zero_division=0)
recall = recall_score(y_test, predicciones, zero_division=0)
f1 = f1_score(y_test, predicciones, zero_division=0)

print("\n===== RESULTADOS DEL MODELO =====")

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")

# 11. Matriz de confusion

print("\n===== MATRIZ DE CONFUSION =====")

matriz = confusion_matrix(
    y_test,
    predicciones,
    labels=[0, 1]
)

print(matriz)

# 12. Reporte de clasificacion

print("\n===== REPORTE DE CLASIFICACION =====")

print(
    classification_report(
        y_test,
        predicciones,
        labels=[0, 1],
        target_names=["Sin riesgo", "Con riesgo"],
        zero_division=0
    )
)

# 13. Guardar el modelo entrenado

os.makedirs("models", exist_ok=True)

joblib.dump(
    modelo,
    "models/modelo_baseline.pkl"
)

print("\nModelo guardado en models/modelo_baseline.pkl")
