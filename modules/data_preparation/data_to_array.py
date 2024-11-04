import numpy as np
import re

def python_list_to_numpy(array):
    
    array_np = np.array(array)

    return array_np


#remueve los espacios de un string
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


def filds_to_elements(array):

    array_len = len(array)
    #matrix = [[""] * 4 for _ in range(array_len)]
    matrix = []

    pattern = r"(\d{2}/\d{2}/\d{4}),(\d{2}:\d{2})-(.*?):(.+)"


    for line in array:
        
        match = re.match(pattern, line.strip())
            
        if match:
            date, time, name, message = match.groups()
            matrix.append([date, time, name, message])


    return matrix
