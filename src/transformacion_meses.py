import pandas as pd

MESES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

# Cargar datos
df = pd.read_csv("data/processed/homicidios_gto_2020_2025_raw.csv")

# Transformar a formato largo
df_long = df.melt(
    id_vars=[
        "Año",
        "Entidad",
        "Municipio",
        "Tipo de delito",
        "Subtipo de delito"
    ],
    value_vars=MESES,
    var_name="Mes",
    value_name="Casos"
)

# Guardar resultado
df_long.to_csv("data/processed/homicidios_gto_2020_2025_long.csv", index=False)

print("Transformación long completada.")
