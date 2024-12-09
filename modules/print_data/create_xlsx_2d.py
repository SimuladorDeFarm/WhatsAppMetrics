import pandas as pd
import numpy as np


def create_xlsx_2d(array, nombre):

    # Crear DataFrame con el índice como días y las frecuencias en una columna
    df = pd.DataFrame(array, columns=['Frecuencia'], index=np.arange(1, len(array) + 1))
    df.index.name = 'Día'

    # Guardar en archivo Excel
    df.to_excel(f"./files/daily_freq_{nombre}.xlsx")

#cycle to create each fild
def create_xlsx_2d_for_all(array, array_members):
    
    for i in range(0, len(array[0])):
        msj_vector  = array[:, i].ravel()
        create_xlsx_2d(msj_vector, array_members[i])
