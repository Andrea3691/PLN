# Instalación de dependencias (ejecutar en terminal si no están instaladas)
# !pip install spacy pandas
# !python -m spacy download es_core_news_sm

import spacy
from spacy import displacy
import pandas as pd

# Carga del modelo estadístico de lenguaje español
# Este modelo permite realizar las predicciones POS y de dependencias
nlp = spacy.load("es_core_news_sm")