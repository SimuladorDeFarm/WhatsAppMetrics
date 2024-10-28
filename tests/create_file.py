import pandas as pd

# Array whot fequencies
frequencies = [5, 7, 3, 8, 6] 

# create DataFrame from a array
df = pd.DataFrame({
    'Día': list(range(1, len(frequencies) + 1)),  # Generates a list of position numbers(1, 2, 3, ...)
    'Frecuencia': frequencies
})

# Guardar el DataFrame en un archivo Excel
df.to_excel('frequencies.xlsx', index=False)

print("Exel file create succesfully.")