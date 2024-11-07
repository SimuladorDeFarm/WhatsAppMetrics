
import pandas as pd
import numpy as np
import re


def create_and_save_csv(array):

    DF = pd.DataFrame(array)

    DF.to_csv("messages.csv")



def convert_txt_to_csv(array):



    create_and_save_csv(array)

    return array