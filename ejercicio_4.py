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
        def reprobrado_seguro(notas):
            if isinstance(notas, list) and len(notas) > 0 and np.any(np.array(notas) < 4.0): # Verifica que notas sea una lista, que no esté vacía y que alguna nota sea menor a 4.0
                return 'Reprobado'
            else:
                return "Aprobado"

        df_estudiantes['reprobados'] = df_estudiantes['notas'].apply(reprobrado_seguro)
        reprobados = np.sum(df_estudiantes['reprobados'] == 'Reprobado')
        porcentaje_reprobados = pd.Series(reprobados / len(df_estudiantes) * 100)
        porcentaje_reprobados = round(porcentaje_reprobados, 1)
        print(f"Porcentaje de estudiantes que reprobaron alguna asignatura: {porcentaje_reprobados.to_string(index=False)}%")
