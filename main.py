from modules.utils import *
import numpy as np
import time
from memory_profiler import profile
import os

import cProfile
import pstats

    
    #shared_link = "https://drive.google.com/file/d/1anBiGlkD8Fj-WBXWRoCoBMpCJGqbdJyc/view?usp=drive_link"

    #test link = https://drive.google.com/file/d/1m9xAsvkPo2qhpiqTLYSD9DT_jMu_Rsfj/view?usp=drive_link
    

    
def title():
    print(r"""
╔════════════════════════════════╗
║                                ║
║       WHATSAPP METRICS         ║
║                                ║
╚════════════════════════════════╝
""")


#@profile
def main():
    
    os.system("clear")


    start_time = time.time()
    
    
    user_directory = Directorio()

    verify_or_create_user_dir(user_directory)
    

    title()
    
    #prepare the data: extract of file, validate data and transform into numpy array
    fileName = "Test" 
    array, array_members, group_name = main_data_preparation()
    

    daily_freq, total_freq = main_data_prosses(array, array_members)

    
    main_print_data(daily_freq, array_members, total_freq, group_name, user_directory)
    
    # Código a medir
    end_time = time.time()
    #print("Tiempo de ejecución:", end_time - start_time, "segundos")

    print()

main()
'''
if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()

    # Guardar y ordenar los resultados en un archivo de texto
    with open("performance_results.txt", "w") as f:
        stats = pstats.Stats(pr, stream=f)
        stats.sort_stats("time").print_stats()
'''