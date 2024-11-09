from modules.data_prosses.measures_of_central_tendency import *
import numpy as np

def test():
    

    # Crear una matriz inicial de 3 filas y 1 columna
    matrix = np.array([1, 2, 3])

    # Agregar una nueva columna
    new_column = np.array([4, 5, 6])
    another_column = np.array([7, 8, 9])

    matrix = np.vstack((matrix, new_column, another_column))

    # Agregar otra columna

    print(matrix)


def print_results(members_array, total_freq):

    for i in range (0, len(members_array)):
        print("total frequency of speak:")
        print(members_array[i], ": ", total_freq[i])


def main_data_prosses(data_matrix, members_array):

    print("Calculando frecuencias...")
    daily_freq = daily_freq_message(data_matrix, members_array )

    total_freq = calculate_total_freq(daily_freq)

    #remove this and move to printing data directory
    print_results(members_array, total_freq)

    return daily_freq