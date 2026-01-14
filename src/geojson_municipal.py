import geopandas as gpd

# Cargar shapefile original (local)
gdf = gpd.read_file(
    "data/geo/raw/municipios_gto/municipios_gto.shp"
)

# Normalizar nombre de municipio
gdf["Municipio_norm"] = (
    gdf["NOMGEO"]
    .str.upper()
    .str.strip()
)

# Conservar solo lo necesario
gdf = gdf[["Municipio_norm", "geometry"]]

# Guardar GeoJSON ligero
gdf.to_file(
    "data/geo/processed/municipios_gto.geojson",
    driver="GeoJSON"
)

print("GeoJSON de municipios generado correctamente.")
