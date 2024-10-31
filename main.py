from modules.utils import *

def main():

    file = load_file()
    messages = line_validator(file)
    #print(messages)

    print(remove_spaces(messages[0]))
    file.close()


if __name__ == "__main__":
    main()