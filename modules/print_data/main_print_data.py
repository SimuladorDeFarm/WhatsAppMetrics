from modules.print_data.create_xlsx_2d      import *
from modules.print_data.print_results       import *
from modules.print_data.convert_txt_to_csv  import *
from modules.print_data.dirs                import *    
from modules.print_data.dirs                import Directorio    


def main_print_data(daily_freq, array_members, total_freq, grup_name, user_directory):

    #print_results(total_freq, array_members)

    

    print("(9/10) Creando archivos...")
    create_xlsx_2d(daily_freq, array_members, grup_name, user_directory)
    print("(10/10) Archivos creados correctamente")
