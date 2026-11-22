
# ==========================================
# SISTEMA DE AUTOMATIZACION DE TAREAS
# PROYECTO STUDENT PERFORMANCE
# ==========================================

import subprocess
import sys
import os
from datetime import datetime


# Directorio principal del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Archivos necesarios para ejecutar el proyecto
ARCHIVOS = [
    "data/raw/student-mat.csv",
    "entrenar_modelo.py",
    "validar_modelo.py",
    "validar_datos.py",
    "explorar_datos.py"
]


# ==========================================
# 1. VERIFICACION DE ARCHIVOS
# ==========================================

def verificar_archivos():

    print("\n===== 1. VERIFICACION DE ARCHIVOS =====")

    for archivo in ARCHIVOS:

        ruta = os.path.join(BASE_DIR, archivo)

        if not os.path.exists(ruta):

            print(f"ERROR: No se encontro {archivo}")
            return False

        print(f"OK: {archivo}")

    return True


# ==========================================
# 2. EJECUCION DE SCRIPTS
# ==========================================

def ejecutar_script(nombre_script, descripcion):

    print(f"\n===== {descripcion} =====")

    resultado = subprocess.run(
        [sys.executable, nombre_script],
        cwd=BASE_DIR
    )

    if resultado.returncode != 0:

        print(f"\nERROR: Fallo la ejecucion de {nombre_script}")
        return False

    print(f"\nOK: {nombre_script} ejecutado correctamente.")

    return True


# ==========================================
# 3. VERIFICACION DEL MODELO GENERADO
# ==========================================

def verificar_modelo():

    print("\n===== 4. VERIFICACION DEL MODELO GENERADO =====")

    ruta_modelo = os.path.join(
        BASE_DIR,
        "models",
        "modelo_baseline.pkl"
    )

    if not os.path.exists(ruta_modelo):

        print("ERROR: No se genero el modelo.")
        return False

    print("OK: El archivo del modelo existe.")

    return True


# ==========================================
# 4. EJECUCION DEL PIPELINE COMPLETO
# ==========================================

def ejecutar_pipeline():

    inicio = datetime.now()

    print("=" * 55)
    print("SISTEMA AUTOMATIZADO STUDENT PERFORMANCE")
    print("=" * 55)

    # Paso 1: verificar archivos
    if not verificar_archivos():
        return False

    # Paso 2: validar datos de entrada
    if not ejecutar_script(
        "validar_datos.py",
        "2. VALIDACION DE DATOS DE ENTRADA"
    ):

        print("\nPROCESO DETENIDO: Los datos no cumplen las reglas.")
        return False

    # Paso 3: entrenar modelo
    if not ejecutar_script(
        "entrenar_modelo.py",
        "3. ENTRENAMIENTO DEL MODELO"
    ):
        return False

    # Paso 4: verificar modelo generado
    if not verificar_modelo():
        return False

    # Paso 5: validar modelo
    if not ejecutar_script(
        "validar_modelo.py",
        "5. VALIDACION DEL MODELO Y METRICAS"
    ):
        return False

    # Paso 6: finalizar proceso
    fin = datetime.now()

    duracion = (fin - inicio).total_seconds()

    print("\n" + "=" * 55)
    print("PROCESO AUTOMATIZADO FINALIZADO")
    print("=" * 55)

    print(f"Fecha: {fin.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Duracion: {duracion:.2f} segundos")
    print("Estado: EXITOSO")

    return True


# ==========================================
# 5. PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================

if __name__ == "__main__":

    exito = ejecutar_pipeline()

    if not exito:
        sys.exit(1)
