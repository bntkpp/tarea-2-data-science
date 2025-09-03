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
        def aprobado_seguro(notas):
            if isinstance(notas, list) and len(notas) > 0 and np.all(np.array(notas) >= 4.0):
                return 'Aprobado'
            else:
                return "Reprobado"

        df_estudiantes['aprobados'] = df_estudiantes['notas'].apply(aprobado_seguro)
        aprobados = (df_estudiantes['aprobados'] == 'Aprobado').sum()

        print(df_estudiantes[['nombre', 'aprobados']].to_string(index=False))
        print(f"Cantidad de estudiantes que aprobaron todas sus asignaturas: {aprobados}")