import requests
import io
import re
from zipfile import ZipFile
import zipfile

#recive un archivo binario, lo transforma a zip, lo descomprime y recoje el .txt qur hay dentro y retorna una lista donde fila es una linea del txt
def byte_to_zip_and_list(zip_data): 
    # Abrir el archivo ZIP
    with ZipFile(zip_data) as zip_file:
        # Listar los nombres de los archivos dentro del ZIP
        file_names = zip_file.namelist()
        

        # Extraer el archivo .txt específico a una variable
        txt_content = None
        for file_name in file_names:
            if file_name.endswith(".txt"):  # Buscar un archivo .txt
                with zip_file.open(file_name) as txt_file:
                    txt_content = txt_file.read().decode("utf-8")  # Leer y decodificar el archivo como texto
                    break  # Detenerse después de encontrar el archivo deseado

        if txt_content:

            #convertir string en una lsita donde cada linea es una fila
            result = txt_content.split("\n")
            return result

        else:
            print("No se encontró un archivo .txt en el ZIP.")

def obtain_group_name(file_name):

    array = file_name.split()
    
    for i in range(0,4):
        array.pop(0)    

    last_element = len(array)-1
    word = array[last_element]
    word = word.replace(".zip", "")
    array[last_element] = word

    return array
    


def load_file_from_gdrive(shared_link):

    # Extraer el ID del archivo del enlace compartido
    file_id = shared_link.split('/d/')[1].split('/')[0]

    # URL de descarga directa de Google Drive
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    
    # Realizar la solicitud de descarga
    with requests.get(download_url, stream=True) as response:
        if response.status_code == 200:
            # Obtener el nombre del archivo del encabezado 'Content-Disposition' (opcional)
            content_disposition = response.headers.get('Content-Disposition')
            if content_disposition:
                filename_match = re.search(r'filename="(.+)"', content_disposition)
                filename = filename_match.group(1) if filename_match else "unknown_file"
            else:
                filename = "unknown_file"
            
            # Cargar el contenido del archivo en memoria
            file_in_memory = io.BytesIO(response.content)
            
            # Retornar el archivo cargado en memoria
            return file_in_memory, filename
        else:
            raise Exception(f"Error al descargar el archivo: {response.status_code}")


def main_obtain_files_wsp(shared_link):
    try:
        binary_file, file_name = load_file_from_gdrive(shared_link)
        group_name_array = obtain_group_name(file_name)
        group_name = " ".join(group_name_array)
        lines = byte_to_zip_and_list(binary_file)
        return lines, group_name

    except Exception as e:
        print(f"Error: {e}")
