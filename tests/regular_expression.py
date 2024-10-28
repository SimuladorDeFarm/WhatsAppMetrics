import re

def es_fecha(texto):
    # Define the pattern of regular expression for formate dd/mm/yy
    patron = r'^\d{2}/\d{2}/\d{4}$'
    
    #check if te text  coincide whit the pattern
    if re.match(patron, texto):
        return True
    else:
        return False

# example
texto1 = "27/12/2023"
texto2 = "27-12-2023"
texto3 = "27 diciembre 2023"

print(f"Texto 1 es fecha: {es_fecha(texto1)}")  # return: True
print(f"Texto 2 es fecha: {es_fecha(texto2)}")  # return: False
print(f"Texto 3 es fecha: {es_fecha(texto3)}")  # return: False