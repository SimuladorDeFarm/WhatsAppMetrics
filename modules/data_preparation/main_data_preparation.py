from modules.data_preparation.data_to_array     import *
from modules.data_preparation.load_file         import *
from modules.data_preparation.validate_data     import *
from modules.data_preparation.identify_members  import *

def main_data_preparation(name):
    
    print("Cargando archivo...")
    file = load_file(name)

    print("validando linea")
    array = array_line_validator(file)

    print("cerrando archivo")
    file.close()
    
    print("removiendo espacios")
    array = remove_spaces_of_list(array)

    print("campos a elementos")
    array = filds_to_elements(array)

    print("array a numpy")
    array = python_list_to_numpy(array)

    print("identificando miembros...")
    array_members = identify_members(array)

    return array, array_members