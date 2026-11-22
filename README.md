# PROYECTO STUDENT PERFORMANCE
## Sistema de clasificación de riesgo académico mediante Machine Learning

### 1. Descripción del proyecto

Este proyecto desarrolla un modelo de clasificación utilizando el dataset Student Performance, correspondiente al desempeño académico de estudiantes en la asignatura de matemáticas.

El objetivo es construir un modelo de aprendizaje automático que permita identificar estudiantes con posible riesgo académico, a partir de sus características personales, familiares y académicas.

Se utiliza un modelo de regresión logística para clasificar a los estudiantes en dos categorías:

- **Con riesgo académico:** calificación final G3 inferior a 10.
- **Sin riesgo académico:** calificación final G3 igual o superior a 10.

El proyecto incorpora mecanismos de validación de datos, automatización del entrenamiento y evaluación del modelo, así como un contrato de datos en formato JSON para futuras predicciones.

### 2. Requisitos técnicos

Para ejecutar el proyecto se necesitan los siguientes componentes:

| Herramienta | Función |
|---|---|
| Python 3.14.2 | Lenguaje de programación utilizado |
| Visual Studio Code | Entorno de desarrollo |
| Pandas | Manipulación y análisis de datos |
| Scikit-learn | Entrenamiento y evaluación del modelo |
| Matplotlib | Visualización de datos |
| Seaborn | Elaboración de gráficos estadísticos |
| Joblib | Almacenamiento y recuperación del modelo |

También se utilizan módulos incluidos en Python, como `csv`, `json`, `os`, `sys` y `subprocess`.

Las dependencias externas y sus versiones se encuentran registradas en el archivo `requirements.txt`.

### 3. Estructura del proyecto

La organización de los archivos es la siguiente:

```text
Actividad 2/
│
├── .venv/
│
├── data/
│   └── raw/
│       ├── student-mat.csv
│       └── student-mat-prueba.csv
│
├── models/
│   └── modelo_baseline.pkl
│
├── explorar_datos.py
├── entrenar_modelo.py
├── validar_modelo.py
├── validar_datos.py
├── run_pipeline.py
├── contrato_datos.json
├── requirements.txt
├── README.md
│
├── Figure_1.png
├── Figure_2.png
├── Figure_3.png
└── Figure_4.png
```

**Descripción de los archivos principales:**

- `student-mat.csv`: dataset original utilizado para el desarrollo y entrenamiento del modelo.
- `student-mat-prueba.csv`: copia del dataset utilizada para realizar pruebas controladas de validación. No es necesaria para ejecutar el entrenamiento.
- `explorar_datos.py`: realiza el análisis exploratorio de los datos.
- `validar_datos.py`: comprueba tipos de datos, valores nulos, rangos y categorías permitidas.
- `entrenar_modelo.py`: prepara los datos, entrena el modelo y calcula las métricas de desempeño.
- `validar_modelo.py`: carga el modelo guardado y realiza su validación funcional.
- `run_pipeline.py`: coordina la ejecución automatizada de las etapas de validación, entrenamiento y evaluación.
- `contrato_datos.json`: define las características y restricciones de las 32 variables de entrada, incluyendo ejemplos válidos e inválidos.
- `requirements.txt`: contiene las dependencias y versiones de las librerías utilizadas.
- `modelo_baseline.pkl`: archivo generado durante el entrenamiento que contiene el modelo ajustado.

Las imágenes `Figure_1.png`, `Figure_2.png`, `Figure_3.png` y `Figure_4.png` corresponden a los recursos gráficos generados durante el desarrollo del proyecto.

**Nota:** la carpeta `.venv` y el archivo `modelo_baseline.pkl` se generan localmente. No es necesario incluirlos en una entrega inicial del código fuente, ya que el entorno virtual se puede reconstruir y el modelo se genera mediante el entrenamiento.

### 4. Instalación y configuración del entorno

Para reproducir el proyecto desde cero, se deben seguir los siguientes pasos.

**Paso 1. Instalar Python**

Instalar Python 3.14.2 y comprobar que se encuentre disponible desde la terminal:

```powershell
python --version
```

**Paso 2. Obtener el proyecto**

Descargar o copiar la carpeta del proyecto `Actividad 2` y abrirla desde Visual Studio Code.

Verificar que el archivo `student-mat.csv` se encuentre en la siguiente ubicación:

```text
data/raw/student-mat.csv
```

**Paso 3. Abrir la terminal en la carpeta principal**

Desde Visual Studio Code, abrir una terminal y ubicarse en la carpeta principal `Actividad 2`.

**Paso 4. Crear el entorno virtual**

Ejecutar:

```powershell
python -m venv .venv
```

**Paso 5. Activar el entorno virtual**

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**Paso 6. Instalar las dependencias**

El proyecto incluye el archivo `requirements.txt`, que contiene las librerías y versiones registradas durante el desarrollo.

Para instalar las dependencias, ejecutar:

```powershell
python -m pip install -r requirements.txt
```

**Paso 7. Verificar las instalaciones**

Ejecutar el siguiente comando:

```powershell
python -c "import pandas, matplotlib, seaborn, sklearn, joblib; print('Dependencias instaladas correctamente')"
```

Si aparece el mensaje de confirmación, las principales dependencias están disponibles en el entorno virtual.

### 5. Preparación de los datos

El archivo `student-mat.csv` debe ubicarse en la siguiente ruta:

```text
data/raw/student-mat.csv
```

El dataset contiene 395 registros y 33 variables.

La variable objetivo se construye a partir de la calificación final G3:

- G3 inferior a 10: riesgo académico (1).
- G3 igual o superior a 10: sin riesgo académico (0).

La variable G3 se utiliza para construir la clasificación y no se incluye entre las variables predictoras del modelo.

Por esta razón, el modelo utiliza 32 variables de entrada y una variable objetivo derivada de la calificación final.

### 6. Ejecución del proyecto

El sistema permite ejecutar las principales etapas del proyecto mediante un solo comando.

Desde la terminal, ubicarse en la carpeta principal `Actividad 2`, activar el entorno virtual y ejecutar:

```powershell
python run_pipeline.py
```

El pipeline desarrolla las siguientes actividades:

1. Verifica la existencia de los archivos necesarios.
2. Ejecuta la validación de los datos de entrada.
3. Entrena el modelo de regresión logística.
4. Comprueba que el archivo del modelo haya sido generado.
5. Ejecuta la validación funcional y calcula las métricas.
6. Muestra el estado final y el tiempo de ejecución.

Si la validación de los datos encuentra inconsistencias, el proceso se detiene antes de iniciar el entrenamiento.

**Ejecución individual de los scripts**

También es posible ejecutar cada archivo de manera independiente:

Análisis exploratorio:

```powershell
python explorar_datos.py
```

Validación de datos:

```powershell
python validar_datos.py
```

Entrenamiento del modelo:

```powershell
python entrenar_modelo.py
```

Validación funcional del modelo:

```powershell
python validar_modelo.py
```

### 7. Lógica de validación de datos

El archivo `validar_datos.py` implementa reglas para verificar:

- Tipos de datos numéricos y categóricos.
- Ausencia de valores nulos.
- Rangos permitidos para las variables numéricas.
- Valores permitidos para las variables categóricas.

La validación se realiza utilizando el módulo estándar `csv` de Python, sin utilizar librerías externas para las comprobaciones.

En la prueba realizada se revisaron 395 registros y no se encontraron errores.

También se realizó una prueba controlada introduciendo un valor de texto en la variable `age`. El sistema identificó la inconsistencia y detuvo el entrenamiento antes de continuar con el pipeline.

Esta funcionalidad permite controlar la calidad de los datos antes de utilizarlos en el entrenamiento del modelo.

### 8. Contrato de datos

El archivo `contrato_datos.json` establece las condiciones que deben cumplir los datos para una futura inferencia del modelo.

Incluye:

- Definición de las 32 variables de entrada.
- Tipos de datos esperados.
- Rangos numéricos y categorías permitidas.
- Un ejemplo de entrada válida.
- Un ejemplo de entrada inválida.

Para comprobar la sintaxis del archivo se utiliza:

```powershell
python -m json.tool contrato_datos.json
```

Para leer su contenido desde Python:

```python
import json

with open("contrato_datos.json", "r", encoding="utf-8") as archivo:
    contrato = json.load(archivo)

print("Contrato de datos cargado correctamente")
```

El contrato funciona como referencia para estandarizar los datos que se utilizarán en futuras predicciones.

La calificación final G3 no forma parte de las 32 variables de entrada, ya que se utiliza para construir la variable objetivo durante el entrenamiento.

### 9. Resultados del modelo

El modelo se entrenó utilizando una división estratificada de los datos:

- Registros de entrenamiento: 316.
- Registros de prueba: 79.
- Proporción de división: 80 % entrenamiento y 20 % prueba.
- Modelo utilizado: regresión logística.

**Métricas obtenidas:**

| Métrica | Resultado |
|---|---:|
| Accuracy | 93,67 % |
| Precision | 95,65 % |
| Recall | 84,62 % |
| F1-score | 89,80 % |

El modelo obtuvo un Accuracy de 93,67 % sobre los datos de prueba.

Los resultados corresponden a una partición específica del dataset y no garantizan el mismo desempeño en otros conjuntos de datos.

La matriz de confusión obtenida fue:

```text
[[52  1]
 [ 4 22]]
```

Estos resultados permiten evaluar el comportamiento del clasificador y su capacidad para identificar estudiantes con riesgo académico.

### 10. Recomendaciones para reproducir el proyecto

Para obtener resultados consistentes se recomienda:

- Mantener la estructura de carpetas definida.
- Utilizar el dataset original `student-mat.csv`.
- No modificar los nombres de las variables del dataset.
- Ejecutar el proyecto desde la carpeta principal.
- Activar el entorno virtual antes de ejecutar los scripts.
- Instalar las dependencias utilizando `requirements.txt`.
- Ejecutar la validación de datos antes del entrenamiento.
- No utilizar `student-mat-prueba.csv` en el entrenamiento, ya que corresponde a una copia empleada para pruebas controladas.
- Conservar el archivo `contrato_datos.json` junto con los demás archivos del proyecto.

### 11. Consideraciones finales

El proyecto integra un proceso de análisis, validación, entrenamiento y evaluación de un modelo de clasificación de riesgo académico.

La automatización permite ejecutar las etapas principales mediante un único comando, mientras que la lógica de validación controla la calidad de los datos antes del entrenamiento.

El contrato JSON establece una estructura de referencia para futuras aplicaciones del modelo y facilita la estandarización de los datos de entrada.

La documentación técnica y el archivo de dependencias permiten que otras personas puedan configurar el entorno, instalar las herramientas necesarias y reproducir el pipeline siguiendo las instrucciones descritas.