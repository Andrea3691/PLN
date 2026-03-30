def ejecutar_analisis_morfologico(texto):
    """
    Transforma el texto en un objeto Doc y extrae etiquetas POS.
    """
    doc = nlp(texto)
    
    # Estructuración de datos para el informe técnico
    analisis = []
    for token in doc:
        analisis.append({
            "Token": token.text,
            "Lema": token.lemma_,
            "POS_Tag": token.pos_,
            "Definicion": spacy.explain(token.pos_),
            "Morfologia": token.morph
        })
    
    return pd.DataFrame(analisis)

# Prueba con el Caso Base (Estructura Simple)
frase_simple = "La IA transforma los datos."
df_morfologia = ejecutar_analisis_morfologico(frase_simple)
print("--- Análisis Morfológico (POS) ---")
print(df_morfologia)