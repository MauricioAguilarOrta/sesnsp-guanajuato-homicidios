import pandas as pd

# Cargar datos
df = pd.read_csv("data/raw/Municipal-Delitos - Noviembre 2025 (2015-2025).csv", encoding="latin-1")

# Filtrar entidad
df = df[df["Entidad"] == "Guanajuato"]

# Filtrar periodo
df = df[
    (df["Año"] >= 2020) &
    (df["Año"] <= 2025)
]

# Filtrar tipo y subtipo de delito
df = df[
    (df["Tipo de delito"] == "Homicidio") &
    (df["Subtipo de delito"].isin([
        "Homicidio doloso",
        "Homicidio culposo"
    ]))
]

# Guardar
df.to_csv("data/processed/homicidios_gto_2020_2025_raw.csv", index=False)

print("Archivo filtrado correctamente.")
