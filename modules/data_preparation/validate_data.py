import re

def file_to_list(file):
    
    line = file.readlines()
    
    return line

def msj_line_validator(text):
    

    # validation hh
    match1 = re.search(r"^\d{2}/\d{2}/\d{4}, \d{2}:\d{2} -.+:.+$", text)
    match2 = re.search(r"^\d{1}/\d{2}/\d{4}, \d{2}:\d{2} -.+:.+$", text)
    match3 = re.search(r"^\d{2}/\d{1}/\d{4}, \d{2}:\d{2} -.+:.+$", text)
    match4 = re.search(r"^\d{1}/\d{1}/\d{4}, \d{2}:\d{2} -.+:.+$", text)
    

    if match1 != None or match2 != None or match3 != None or match4 != None  :
        return True
    else:
        return False


def array_line_validator(file):

    lines = file_to_list(file)

    i = 0    
    while i < len(lines):

        if msj_line_validator(lines[i]) == False:
            del lines[i]
            i-=1
        
        i+=1
    
    return lines
    

