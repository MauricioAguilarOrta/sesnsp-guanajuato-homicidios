import pandas as pd

# Cargar datos
df = pd.read_csv("data/processed/homicidios_gto_2020_2025_long.csv")

# Agregar casos por municipio, año y subtipo
df_municipal_anual = (
    df.groupby(
        ["Municipio", "Año", "Subtipo de delito"],
        as_index=False
    )["Casos"]
    .sum()
)

# Guardar resultado
df_municipal_anual.to_csv("data/processed/homicidios_gto_2020_2025_municipal_anual.csv"
, index=False)

print("Agregación municipal anual completada.")
