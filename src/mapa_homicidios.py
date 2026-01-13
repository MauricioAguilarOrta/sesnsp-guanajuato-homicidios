import pandas as pd
import geopandas as gpd
import folium

# 1. Cargar datos de homicidios (municipal anual)
df = pd.read_csv(
    "data/processed/homicidios_gto_2020_2025_municipal_anual.csv"
)

# Normalizar nombre de municipio
df["Municipio_norm"] = (
    df["Municipio"]
    .str.upper()
    .str.strip()
)

# 2. Cargar shapefile de municipios
gdf = gpd.read_file(
    "data/geo/municipios_gto/municipios_gto.shp"
)

# Normalizar nombre de municipio en shapefile
gdf["Municipio_norm"] = (
    gdf["NOMGEO"]
    .str.upper()
    .str.strip()
)

# 3. Join datos + geometría
gdf_homicidios = gdf.merge(
    df,
    on="Municipio_norm",
    how="left"
)

# 4. Cargar población municipal (placeholder)
df_pob = pd.read_csv(
    "data/poblacion/poblacion_municipal_gto.csv"
)

df_pob["Municipio_norm"] = (
    df_pob["Municipio"]
    .str.upper()
    .str.strip()
)

# Unir población
gdf_homicidios = gdf_homicidios.merge(
    df_pob[["Municipio_norm", "Poblacion"]],
    on="Municipio_norm",
    how="left"
)

# 5. Calcular tasa por 100 mil habitantes
gdf_homicidios["Tasa_x_100mil"] = (
    gdf_homicidios["Casos"] / gdf_homicidios["Poblacion"]
) * 100000

# 6. Seleccionar corte para el mapa
ANIO = 2025
SUBTIPO = "Homicidio doloso"

gdf_mapa = gdf_homicidios[
    (gdf_homicidios["Año"] == ANIO) &
    (gdf_homicidios["Subtipo de delito"] == SUBTIPO)
]

# 7. Crear mapa base
m = folium.Map(
    location=[21.0, -101.0],
    zoom_start=8,
    tiles="cartodbpositron"
)

# 8. Agregar capa coroplética (tasas)
folium.Choropleth(
    geo_data=gdf_mapa,
    data=gdf_mapa,
    columns=["Municipio_norm", "Tasa_x_100mil"],
    key_on="feature.properties.Municipio_norm",
    fill_color="Reds",
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name=f"Tasa de {SUBTIPO} por 100 mil hab. ({ANIO})"
).add_to(m)

# 9. Tooltip con información municipal
tooltip = folium.GeoJsonTooltip(
    fields=[
        "NOMGEO",
        "Año",
        "Subtipo de delito",
        "Casos",
        "Tasa_x_100mil"
    ],
    aliases=[
        "Municipio:",
        "Año:",
        "Subtipo:",
        "Casos:",
        "Tasa por 100 mil:"
    ],
    localize=True,
    sticky=False,
    labels=True
)

folium.GeoJson(
    gdf_mapa,
    tooltip=tooltip,
    name="Detalle municipal",
    style_function=lambda x: {
        "fillOpacity": 0,
        "color": "transparent",
        "weight": 0
    }
).add_to(m)

# 10. Guardar mapa (SIEMPRE AL FINAL)
m.save("outputs/mapa_homicidios_gto_tasas.html")

print("Mapa con tasas y tooltip generado correctamente.")
