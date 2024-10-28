import pandas as pd

# Supongamos que tienes un array con la frecuencia de eventos por día
frecuencias = [5, 7, 3, 8, 6]  # Ejemplo de datos

# Crear un DataFrame a partir del array
df = pd.DataFrame({
    'Día': list(range(1, len(frecuencias) + 1)),  # Genera una lista de números de posición (1, 2, 3, ...)
    'Frecuencia': frecuencias
})

# Guardar el DataFrame en un archivo Excel
df.to_excel('frecuencias.xlsx', index=False)

print("Archivo Excel creado exitosamente.")