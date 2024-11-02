from modules.create_csv.clean_data import remove_spaces, remove_spaces_of_list, filds_to_elements


def convert_txt_to_csv(array):

    array_whitout_spaces = remove_spaces_of_list(array)

    filds_to_elements(array_whitout_spaces)


    return array_whitout_spaces