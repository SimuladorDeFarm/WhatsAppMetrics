import re

def es_fecha(texto):
    # Definir el patrón de la expresión regular para el formato dd/mm/yyyy
    patron = r'^\d{2}/\d{2}/\d{4}$'
    
    # Comprobar si el texto coincide con el patrón
    if re.match(patron, texto):
        return True
    else:
        return False

# Ejemplos de uso
texto1 = "27/12/2023"
texto2 = "27-12-2023"
texto3 = "27 diciembre 2023"

print(f"Texto 1 es fecha: {es_fecha(texto1)}")  # Salida: True
print(f"Texto 2 es fecha: {es_fecha(texto2)}")  # Salida: False
print(f"Texto 3 es fecha: {es_fecha(texto3)}")  # Salida: False