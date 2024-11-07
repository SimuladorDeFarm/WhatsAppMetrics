import numpy as np
from modules.data_preparation.data_to_array import python_list_to_numpy

def daily_freq_message(data_matrix, member_unique_array):

    date_vector = data_matrix[:, 0].ravel()
    msj_vector  = data_matrix[:, 2].ravel()
    
    date_vector_unique = np.unique(date_vector)

    
    number_of_days = len(date_vector_unique)
    print("cantidad de dias",number_of_days)

    len_msj_vector  = len(msj_vector)
    len_date_vector = len(date_vector)
    len_member_unique_array = len(member_unique_array)

    v_aux = [0] * len_member_unique_array
    frequency = [[0] * len_member_unique_array  for _ in range(number_of_days)]
#    frequency = [0] * len_member_unique_array
    dia = 0
    
    for i in range (0, len_msj_vector):

        for j in range(0, len_member_unique_array):
            
            if msj_vector[i] == member_unique_array[j]:
                member = j

        if i == 0:
            frequency[dia][member] = frequency[dia][member] + 1
        else:
            if date_vector[i] == date_vector[i-1]:
                frequency[dia][member] = frequency[dia][member] + 1
            else:
                dia+=1
                frequency[dia][member] = frequency[dia][member] + 1

    frequency = python_list_to_numpy(frequency)
    #print(frequency)

    return frequency
    #for i in range (0, )