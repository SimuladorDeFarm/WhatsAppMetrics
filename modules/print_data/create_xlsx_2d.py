import pandas as pd
import numpy as np


def create_xlsx_2d(array, nombre, grup_name, user_directory):


    # Crear DataFrame con el índice como días y las frecuencias en una columna
    df = pd.DataFrame(array, columns=nombre)
    df.index.name = 'Día'

    # saved in exel file
    df.to_excel(f"{user_directory.get_directory()}/user_daily_freq_{grup_name}.xlsx")

#cycle to create each fild 
def create_xlsx_2d_for_all(array, array_members):
    
    #As many cycle according to ammount members
    #for i in range(0, len(array[0])):
        #msj_vector  = array[:, i].ravel()
    create_xlsx_2d(array, array_members, grup_name)
