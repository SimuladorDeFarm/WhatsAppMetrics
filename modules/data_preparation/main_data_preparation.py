from modules.data_preparation.filds_to_elements import *
from modules.data_preparation.load_file         import *
from modules.data_preparation.validate_data     import *
from modules.data_preparation.identify_members  import *
from modules.data_preparation.obtainFileWsp     import *
from modules.data_preparation.input             import *

def main_data_preparation():
    
    shared_link = inputLink()

    print("(1/10) Cargando archivo...")
    lines, group_name = main_obtain_files_wsp(shared_link)

    print("(2/10) Validando datos...")
    array = array_line_validator(lines)
    
    print("(3/10) Removiendo espacios...")
    array = remove_spaces_of_list(array)

    print("(4/10) Campos a elementos...")
    array = filds_to_elements(array)

    print("(5/10) Array a numpy...")
    array = python_list_to_numpy(array)

    print("(6/10) Identificando miembros...")
    array_members = identify_members(array)

    return array, array_members, group_name