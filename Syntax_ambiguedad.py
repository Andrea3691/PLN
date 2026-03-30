def analizar_resolucion_ambiguedad(texto):
    """
    Analiza las relaciones de dependencia para mitigar la ambigüedad sintáctica.
    """
    doc = nlp(texto)
    
    print(f"\n{'Hijo (Token)':<15} | {'Relación':<12} | {'Padre (Cabeza)':<15}")
    print("-" * 50)
    
    for token in doc:
        print(f"{token.text:<15} | {token.dep_:<12} | {token.head.text:<15}")
    
    # Renderización del árbol sintáctico (Ideal para el Live Demo)
    # Nota: En Jupyter Notebook usa jupyter=True
    displacy.render(doc, style="dep", options={'distance': 100})

# Prueba con el Caso Complejo (Ambigüedad de Adjunto)
frase_ambigua = "El ingeniero observó el modelo con el microscopio."
analizar_resolucion_ambiguedad(frase_ambigua)