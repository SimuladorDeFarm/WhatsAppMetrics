from modules.print_data.create_xlsx_2d import *
from modules.print_data.print_results import *
from modules.print_data.convert_txt_to_csv import *

def main_print_data(daily_freq, array_members, total_freq):

    print_results(total_freq, array_members)



    print("creando archivos...")
    create_xlsx_2d_for_all(daily_freq, array_members)
    print("Archivos creados correctamente")
