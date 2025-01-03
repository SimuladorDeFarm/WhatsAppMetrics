import numpy as np
from modules.data_preparation.parsing.array_parser import python_list_to_numpy

# metodo de fuersza fruta es ineficiente, se deor mucho
def remove_date_repeated(l):
    #len(l) es necesario porque al ir eliminando el largo se va modifciando
    print("removiendo datos repetidos...")
    for i in range (0, len(l) - 1):
        j = i + 1

        while j < len(l):            
            
            if l[i] == l[j]:
                

                l = np.delete(l, j)
            else:
                j = j + 1

    return l
 

def calculate_total_freq(daily_freq):

    len_row_daily_freq = len(daily_freq)
    len_column_daily_freq = len(daily_freq[0])
    
    total_freq = []
    
    for i in range (0, len_column_daily_freq):
        #row = daily_freq[:, i].ravel()
        total_freq.append(0)
        for j in range (0, len_row_daily_freq):
            
            total_freq[i]  = total_freq[i] + daily_freq[j][i]
    
    #total_freq.sort(reverse=True)
        
    total_freq = python_list_to_numpy(total_freq)
    
    return total_freq      



def daily_freq_message(data_matrix, member_unique_array):

    date_vector = data_matrix[:, 0].ravel()
    msj_vector  = data_matrix[:, 2].ravel()
    
    #obtiene un array de las fechas sin repetir al aprecer esta malo
    #date_vector_unique = np.unique(date_vector)



    #contar cantidad de dias
    #number_of_days = len(date_vector_unique)
    
    #i maked the function manually but result what the original was god
    date_vector_unique = np.unique(date_vector)
    
    #date_vector_unique = remove_date_repeated(date_vector)
    number_of_days = len(date_vector_unique)
    

    len_msj_vector  = len(msj_vector)
    len_date_vector = len(date_vector)
    len_member_unique_array = len(member_unique_array)

    v_aux = [0] * len_member_unique_array
    frequency = [[0] * len_member_unique_array  for _ in range(number_of_days)]
#    frequency = [0] * len_member_unique_array
    dia = 0

   
    
    for i in range (0, len_msj_vector):
        
        #imprimir cuantos calculos  lleva
        if (i % 100 == 0) or (i == len_msj_vector - 1):
            print(f"\r  ({i + 1}/{len_msj_vector}) calculando frecuencias diarias... ", end="", flush=True) 

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
    print()
    #print(frequency)
   
    return frequency
    #for i in range (0, )