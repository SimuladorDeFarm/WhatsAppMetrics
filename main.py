from modules.utils import *
import numpy as np
import time
from memory_profiler import profile

import cProfile
import pstats

@profile
def main():
    
    start_time = time.time()

    #prepare the data: extract of file, validate data and transform into numpy array
    array, array_members = main_data_preparation()
    
    #convert_txt_to_csv(array)

    daily_freq = main_data_prosses(array, array_members)


    #main_print_data(daily_freq, array_members)
    
    # Código a medir
    end_time = time.time()
    print("Tiempo de ejecución:", end_time - start_time, "segundos")


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()

    # Guardar y ordenar los resultados en un archivo de texto
    with open("performance_results.txt", "w") as f:
        stats = pstats.Stats(pr, stream=f)
        stats.sort_stats("time").print_stats()
