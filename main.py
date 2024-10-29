from modules.files.load_file import load_file
from modules.files.convert_txt_to_csv import file_to_list
from modules.files.convert_txt_to_csv import line_validator


file = load_file()

print(line_validator(file))

file.close() 
