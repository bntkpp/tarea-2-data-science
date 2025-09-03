from datos_estudiantes import estudiantes
import statistics
import pandas as pd
import numpy as np

if estudiantes == []:
    print("No hay estudiantes")
else:
    df_estudiantes = pd.DataFrame(estudiantes)
    
    # Verifica si todas las listas de notas están vacías
    if df_estudiantes['notas'].apply(lambda x: len(x) == 0).all():
        print("No hay notas")
    else:
        notas = df_estudiantes['notas'].explode()
        moda = pd.Series(notas).mode().to_string(index=False)
        print(f"La moda de las notas es: {moda}")