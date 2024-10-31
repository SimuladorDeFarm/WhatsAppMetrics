from modules.create_csv.clean_data import remove_spaces, remove_spaces_of_list


def convert_txt_to_csv(array):

    array_whitout_spaces = remove_spaces_of_list(array)
        
    return array_whitout_spaces