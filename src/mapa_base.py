import geopandas as gpd
import pandas as pd

# Cargar shapefile
gdf_mapa = gpd.read_file(
    "data/geo/municipios_gto/municipios_gto.shp"
)

print("Columnas del shapefile:")
print(gdf_mapa.columns)

# Cargar datos municipales
df = pd.read_csv(
    "data/processed/homicidios_gto_2020_2025_municipal.csv"
)

print("\nColumnas de datos:")
print(df.columns)

# Vista rápida
print("\nPrimeras filas del shapefile:")
print(gdf_mapa.head())

print("\nPrimeras filas de los datos:")
print(df.head())