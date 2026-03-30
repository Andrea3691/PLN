# PLN
# Análisis de Niveles Lingüísticos y Resolución de Ambigüedad con IA

Este repositorio contiene la implementación práctica y el código fuente correspondiente al **Grupo 1** para el proyecto de Procesamiento de Lenguaje Natural (PLN). El objetivo principal es analizar los niveles lingüísticos (morfológico y sintáctico) y demostrar cómo la Inteligencia Artificial resuelve la ambigüedad sintáctica utilizando la librería `spaCy`.

## 📋 Descripción del Proyecto
El código implementa un *pipeline* de procesamiento lingüístico que toma oraciones en lenguaje natural (español) y realiza:
1. **Tokenización y Lematización:** Descomposición del texto y extracción de la raíz de las palabras.
2. **Part-of-Speech (POS) Tagging:** Asignación de categorías gramaticales (sustantivos, verbos, determinantes, etc.).
3. **Dependency Parsing:** Creación de árboles de dependencias sintácticas para identificar al "padre" e "hijo" de cada palabra, resolviendo así casos de ambigüedad en oraciones complejas.

## 🛠️ Requisitos del Sistema
Para garantizar la reproducibilidad del entorno de desarrollo, se requiere:
* **Sistema Operativo:** Windows (con WSL recomendado), Linux o macOS.
* **Lenguaje:** Python 3.8 o superior.
* **Gestor de paquetes:** `pip`.

##  Librerías y Dependencias Específicas
El proyecto utiliza las siguientes librerías de Python. Se recomienda usar un entorno virtual (`venv` o `conda`).

* `spacy` (v3.x): Motor principal para el procesamiento de lenguaje natural.
* `pandas`: Utilizado para la estructuración y visualización tabular de los datos morfológicos.
* `jupyter` o `notebook`: Para la ejecución del entorno interactivo y visualización del código paso a paso.
* **Modelo Estadístico:** `es_core_news_sm` (Pipeline optimizado para español de spaCy).

### Archivo `requirements.txt`
Si deseas crear un archivo `requirements.txt`, su contenido debe ser:
```text
spacy>=3.5.0
pandas>=2.0.0
jupyter>=1.0.0
