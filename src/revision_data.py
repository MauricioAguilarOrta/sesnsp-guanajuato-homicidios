import pandas as pd

# Ruta al archivo CSV
FILE_PATH = "data/raw/Municipal-Delitos - Noviembre 2025 (2015-2025).csv"

# Cargar datos
df = pd.read_csv(FILE_PATH, encoding="latin-1")

# Información básica
print("Dimensiones del dataset (filas, columnas):")
print(df.shape)

print("\nPrimeras 5 filas:")
print(df.head())

print("\nNombres de las columnas:")
for col in df.columns:
    print("-", col)
