from datos_estudiantes import estudiantes
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
        def promedio_seguro(notas):
            if isinstance(notas, list) and len(notas) > 0: # Verifica que notas sea una lista y que no esté vacía
                return round(np.mean(notas), 1) # Calcula el promedio de las notas
            else:
                return "No hay notas"
            
        df_estudiantes['promedio'] = df_estudiantes['notas'].apply(promedio_seguro)
        promedios = df_estudiantes['promedio']
        nota_maxima = df_estudiantes['promedio'].max()
        nota_minima = df_estudiantes['promedio'].min()

        print(df_estudiantes[['nombre', 'promedio']].to_string(index=False))
        print(f"Promedio máxima: {nota_maxima}")
        print(f"Promedio mínima: {nota_minima}")