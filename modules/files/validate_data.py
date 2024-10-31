import re

def file_to_list(file):
    
    line = file.readlines()
    
    return line

def msj_line_validator(text):
    
    # validation hh
    match = re.search(r"^\d{1,2}/\d{1,2}/\d{4}, \d{2}:\d{2} -.+:.+$", text)
    
    if match == None:
        return False
    else:
        return True

def line_validator(file):

    lines = file_to_list(file)

    i = 0    
    while i < len(lines):

        if msj_line_validator(lines[i]) == False:
            del lines[i]
            i-=1
        
        i+=1

    return lines
    

