# Agregación anual de homicidios por municipio y subtipo de delito (Guanajuato, 2020–2025)
import pandas as pd

# Cargar datos
df = pd.read_csv("data/processed/homicidios_gto_2020_2025_long.csv")

# Agregar casos por municipio y subtipo
df_municipal = (
    df.groupby(
        ["Municipio", "Subtipo de delito"],
        as_index=False
    )["Casos"]
    .sum()
)

# Guardar resultado
df_municipal.to_csv("data/processed/homicidios_gto_2020_2025_municipal.csv"
, index=False)

print("Agregación municipal completada.")
