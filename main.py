from modules.utils import *
import numpy as np

def main():

    #prepare the data: extract of file, validate data and transform into numpy array
    array, array_members = main_data_preparation()
    
    #convert_txt_to_csv(array)

    main_data_prosses(array, array_members)

if __name__ == "__main__":
    main()