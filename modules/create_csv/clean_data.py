
def remove_spaces(string):

    string_whithout_space = string.replace(" ", "")

    return string_whithout_space


# traverse the array and call remove_space to remove spaces in onle line
def remove_spaces_of_list(array):
    
    array_len = len(array)
    
    array_without_spaces = []
    
    i = 0
    while i < array_len:
        array_without_spaces.append(remove_spaces(array[i]))
        
        i+=1
    
    return array_without_spaces