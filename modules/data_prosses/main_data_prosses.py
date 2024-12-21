from modules.data_prosses.measures_of_central_tendency import *
import numpy as np



def main_data_prosses(data_matrix, members_array):

    print("(7/10) Calculando frecuencias...")
    daily_freq = daily_freq_message(data_matrix, members_array )

    total_freq = calculate_total_freq(daily_freq)

    #remove this and move to printing data directory
    #print_results(members_array, total_freq)

    return daily_freq, total_freq