
# ==========================================
# VALIDACION DE DATOS DE ENTRADA
# PROYECTO STUDENT PERFORMANCE
# ==========================================

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RUTA_DATASET = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "student-mat.csv"
)

# Variables numericas y sus rangos permitidos
RANGOS = {
    "age": (15, 22),
    "Medu": (0, 4),
    "Fedu": (0, 4),
    "traveltime": (1, 4),
    "studytime": (1, 4),
    "failures": (0, 3),
    "famrel": (1, 5),
    "freetime": (1, 5),
    "goout": (1, 5),
    "Dalc": (1, 5),
    "Walc": (1, 5),
    "health": (1, 5),
    "absences": (0, 365),
    "G1": (0, 20),
    "G2": (0, 20),
    "G3": (0, 20)
}

# Valores permitidos para variables categoricas
CATEGORIAS = {
    "school": {"GP", "MS"},
    "sex": {"F", "M"},
    "address": {"U", "R"},
    "famsize": {"LE3", "GT3"},
    "Pstatus": {"T", "A"},
    "Mjob": {"teacher", "health", "services", "at_home", "other"},
    "Fjob": {"teacher", "health", "services", "at_home", "other"},
    "reason": {"home", "reputation", "course", "other"},
    "guardian": {"mother", "father", "other"},
    "schoolsup": {"yes", "no"},
    "famsup": {"yes", "no"},
    "paid": {"yes", "no"},
    "activities": {"yes", "no"},
    "nursery": {"yes", "no"},
    "higher": {"yes", "no"},
    "internet": {"yes", "no"},
    "romantic": {"yes", "no"}
}


def validar_datos():

    print("\n===== VALIDACION DE DATOS DE ENTRADA =====")

    errores = []
    registros = 0

    if not os.path.exists(RUTA_DATASET):
        print("ERROR: No se encontro el archivo del dataset.")
        return False

    with open(RUTA_DATASET, "r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo, delimiter=";")

        columnas = lector.fieldnames

        if not columnas:
            print("ERROR: El dataset no contiene encabezados.")
            return False

        # Verificar que existan las 33 variables esperadas
        columnas_esperadas = set(RANGOS) | set(CATEGORIAS)

        faltantes = columnas_esperadas - set(columnas)

        if faltantes:
            print("ERROR: Faltan columnas:", faltantes)
            return False

        for numero_fila, fila in enumerate(lector, start=2):

            registros += 1

            for columna in columnas_esperadas:

                valor = fila.get(columna)

                # 1. Verificar valores nulos
                if valor is None or valor.strip() == "":
                    errores.append(
                        f"Fila {numero_fila}: {columna} esta vacia."
                    )
                    continue

                # 2. Verificar tipos y rangos numericos
                if columna in RANGOS:

                    try:
                        numero = int(valor)

                        minimo, maximo = RANGOS[columna]

                        if numero < minimo or numero > maximo:
                            errores.append(
                                f"Fila {numero_fila}: {columna} "
                                f"fuera de rango ({valor}). "
                                f"Permitido: {minimo}-{maximo}."
                            )

                    except ValueError:
                        errores.append(
                            f"Fila {numero_fila}: {columna} "
                            f"debe ser un numero entero."
                        )

                # 3. Verificar categorias permitidas
                elif columna in CATEGORIAS:

                    if valor not in CATEGORIAS[columna]:
                        errores.append(
                            f"Fila {numero_fila}: valor '{valor}' "
                            f"no permitido en {columna}."
                        )

    print("\n===== RESULTADOS DE VALIDACION =====")
    print(f"Registros revisados: {registros}")
    print(f"Errores encontrados: {len(errores)}")

    if errores:

        print("\n===== DETALLE DE ERRORES =====")

        for error in errores:
            print(error)

        print("\nVALIDACION FINALIZADA CON ERRORES.")
        return False

    else:

        print("OK: Tipos de datos correctos.")
        print("OK: No se encontraron valores nulos.")
        print("OK: Rangos y categorias correctos.")
        print("\nVALIDACION EXITOSA.")

        return True


if __name__ == "__main__":

    resultado = validar_datos()

    if not resultado:
        raise SystemExit(1)
