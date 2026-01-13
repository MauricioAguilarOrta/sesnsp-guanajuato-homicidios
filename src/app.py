import os
import subprocess
import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Homicidios en Guanajuato",
    layout="wide"
)

st.title("Homicidios en Guanajuato (2020–2025)")
st.caption("Visualización exploratoria con tasas por 100 mil habitantes")

# Cargar datos
if not os.path.exists("data/processed/homicidios_gto_2020_2025_municipal_anual.csv"):
    subprocess.run(
    ["python3", "src/agregacion_municipal_anual.py"],
    check=True)
    subprocess.run(["python3", "src/filtrado_homicidios.py"], check=True)
    subprocess.run(["python3", "src/transformacion_meses.py"], check=True)
    subprocess.run(["python3", "src/agregacion_municipal_anual.py"], check=True)

df = pd.read_csv(
    "data/processed/homicidios_gto_2020_2025_municipal_anual.csv"
)

df["Municipio_norm"] = (
    df["Municipio"]
    .str.upper()
    .str.strip()
)

gdf = gpd.read_file(
    "data/geo/municipios_gto/municipios_gto.shp"
)

gdf["Municipio_norm"] = (
    gdf["NOMGEO"]
    .str.upper()
    .str.strip()
)

df_pob = pd.read_csv(
    "data/poblacion/poblacion_municipal_gto.csv"
)

df_pob["Municipio_norm"] = (
    df_pob["Municipio"]
    .str.upper()
    .str.strip()
)

# Uniones
gdf_homicidios = (
    gdf
    .merge(df, on="Municipio_norm", how="left")
    .merge(
        df_pob[["Municipio_norm", "Poblacion"]],
        on="Municipio_norm",
        how="left"
    )
)

gdf_homicidios["Tasa_x_100mil"] = (
    gdf_homicidios["Casos"] / gdf_homicidios["Poblacion"]
) * 100000

# Selectores (interactividad mínima)
anio = st.selectbox(
    "Selecciona el año",
    sorted(gdf_homicidios["Año"].dropna().unique())
)

subtipo = st.selectbox(
    "Selecciona el subtipo de delito",
    ["Homicidio doloso", "Homicidio culposo"]
)

# Filtrar datos
gdf_mapa = gdf_homicidios[
    (gdf_homicidios["Año"] == anio) &
    (gdf_homicidios["Subtipo de delito"] == subtipo)
]

# Crear mapa
m = folium.Map(
    location=[21.0, -101.0],
    zoom_start=8,
    tiles="cartodbpositron"
)

folium.Choropleth(
    geo_data=gdf_mapa,
    data=gdf_mapa,
    columns=["Municipio_norm", "Tasa_x_100mil"],
    key_on="feature.properties.Municipio_norm",
    fill_color="Reds",
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name=f"Tasa de {subtipo} por 100 mil hab. ({anio})"
).add_to(m)

tooltip = folium.GeoJsonTooltip(
    fields=[
        "NOMGEO",
        "Casos",
        "Tasa_x_100mil"
    ],
    aliases=[
        "Municipio:",
        "Casos:",
        "Tasa por 100 mil:"
    ],
    localize=True,
    labels=True
)

folium.GeoJson(
    gdf_mapa,
    tooltip=tooltip,
    style_function=lambda x: {
        "fillOpacity": 0,
        "color": "transparent",
        "weight": 0
    }
).add_to(m)

st_folium(m, width=1000, height=600)
