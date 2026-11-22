
# ==========================================
# VALIDACION FUNCIONAL DEL MODELO
# PROYECTO STUDENT PERFORMANCE
# ==========================================

import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

print("\n===== VALIDACION FUNCIONAL DEL MODELO =====")

# 1. Definir rutas
ruta_modelo = Path("models/modelo_baseline.pkl")
ruta_datos = Path("data/raw/student-mat.csv")

# 2. Verificar archivos
if not ruta_modelo.exists():
    raise FileNotFoundError("No se encontro el modelo.")

if not ruta_datos.exists():
    raise FileNotFoundError("No se encontro el dataset.")

# 3. Cargar modelo
modelo = joblib.load(ruta_modelo)

print("OK: Modelo cargado correctamente.")

# 4. Cargar dataset
df = pd.read_csv(ruta_datos, sep=";")

# 5. Crear variable objetivo
df["riesgo_academico"] = (df["G3"] < 10).astype(int)

X = df.drop(columns=["G3", "riesgo_academico"])
y = df["riesgo_academico"]

# 6. Reconstruir la division original
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n===== DATOS DE VALIDACION =====")
print("Registros de prueba:", len(X_test))

# 7. Generar predicciones sobre datos de prueba
predicciones = modelo.predict(X_test)

# 8. Calcular metricas
accuracy = accuracy_score(y_test, predicciones)
precision = precision_score(y_test, predicciones, zero_division=0)
recall = recall_score(y_test, predicciones, zero_division=0)
f1 = f1_score(y_test, predicciones, zero_division=0)

print("\n===== METRICAS DE VALIDACION =====")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")

# 9. Matriz de confusion
print("\n===== MATRIZ DE CONFUSION =====")
print(confusion_matrix(y_test, predicciones, labels=[0, 1]))

# 10. Reporte de clasificacion
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

# 11. Mostrar primeras 10 predicciones
resultados = pd.DataFrame({
    "Riesgo_real": y_test.iloc[:10].values,
    "Riesgo_predicho": predicciones[:10]
})

print("\n===== PRIMERAS 10 PREDICCIONES =====")
print(resultados.to_string(index=False))

coincidencias = (
    resultados["Riesgo_real"] ==
    resultados["Riesgo_predicho"]
).sum()

print("\nCoincidencias en las primeras 10:",
      coincidencias, "de 10")

print("\nVALIDACION FUNCIONAL FINALIZADA.")
