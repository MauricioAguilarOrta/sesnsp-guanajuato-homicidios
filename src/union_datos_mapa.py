import geopandas as gpd
import pandas as pd
import unicodedata

# Función para normalizar texto
def normalizar_texto(texto):
    if pd.isna(texto):
        return texto
    texto = texto.upper().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto

# Cargar shapefile
gdf = gpd.read_file(
    "data/geo/municipios_gto/municipios_gto.shp"
)

gdf["mun_norm"] = gdf["NOMGEO"].apply(normalizar_texto)

# Cargar datos agregados
df = pd.read_csv(
    "data/processed/homicidios_gto_2020_2025_municipal.csv"
)

df["mun_norm"] = df["Municipio"].apply(normalizar_texto)

# Join
gdf_join = gdf.merge(
    df,
    on="mun_norm",
    how="left"
)

# Verificación
print("Municipios en shapefile:", gdf.shape[0])
print("Municipios con datos:", gdf_join["Casos"].notna().sum())

print("\nEjemplo de filas unidas:")
print(
    gdf_join[
        ["NOMGEO", "Municipio", "Subtipo de delito", "Casos"]
    ].head(200)
)

