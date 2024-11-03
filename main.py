from modules.utils import *

def main():

    file = load_file()
    messages = array_line_validator(file)
    

    
    print(convert_txt_to_csv(messages))



    file.close()

if __name__ == "__main__":
    main()