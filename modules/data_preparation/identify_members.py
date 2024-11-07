import numpy as np
from modules.data_preparation.data_to_array import python_list_to_numpy
#data_array.shape[0] return leng of rows
#data_array.shape[1] return leng of columns

def imprimir_matriz_j(array, n):
    
    array_len = len(array)
    i = 0
    while i < array_len:
        print(array[i][2])
        i+=1


#retorn list whit users without repeating
def identify_members(data_array):
    
    # currentply members is in i = 2
    members = 2

    #obtain how many rows have  
    data_array_row_len = data_array.shape[0]

    array_members = []
    array_members.append(data_array[0][members])

    #recorring data_array and compare if one member is identificate, if not, is added
    for i in range(1, data_array_row_len):

        is_in = False
        for j in range (0, len(array_members)):

            if data_array[i][members] == array_members[j]:
                is_in = True
        
        if not is_in: 

            array_members.append(data_array[i][members])

    
    array_members = python_list_to_numpy(array_members)

    return array_members


    