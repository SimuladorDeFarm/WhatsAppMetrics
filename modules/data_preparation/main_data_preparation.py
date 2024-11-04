from modules.data_preparation.data_to_array import *
from modules.data_preparation.load_file     import *
from modules.data_preparation.validate_data import *

def main_data_preparation():
    
    file = load_file()

    array = array_line_validator(file)

    file.close()
    
    array = remove_spaces_of_list(array)

    array = filds_to_elements(array)

    array = python_list_to_numpy(array)


    return array