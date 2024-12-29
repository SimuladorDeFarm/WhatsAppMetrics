import os
from platformdirs import *

class Directorio:
    def __init__(self):
        self.directory =  user_documents_dir() + "/WhatsApp Metrics"
        self.defoult_dir = user_documents_dir() + "/WhatsApp Metrics"


    def get_directory(self):
        return self.directory
    
    def set_directory(self, new_directory):
        self.directory = new_directory

    def get_defoult_dir(self):
        return self.defoult_dir

    def reset_directory(self):
        self.directory = self.get_defoult_dir()



def verify_or_create_user_dir(user_directory):

    if not os.path.exists(user_directory.directory):
        os.mkdir(user_directory.directory)
        print(f"Se a creado directorio en: {user_directory.directory} ")
    else:
        print(f"Ruta archivos: {user_directory.directory} ")
        #print("directorio ya existe")

