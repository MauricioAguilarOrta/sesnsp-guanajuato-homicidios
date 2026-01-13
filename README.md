# Homicidios en Guanajuato (SESNSP) – Análisis espacial y temporal

Este repositorio contiene un pipeline reproducible de análisis y visualización de **incidencia de homicidios en el estado de Guanajuato**, utilizando información administrativa oficial del **Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública (SESNSP)**.

El proyecto está enfocado en:
- Limpieza y transformación de registros administrativos de delitos
- Agregación de información a nivel municipal y anual
- Cálculo de tasas por cada 100 mil habitantes
- Visualización espacial interactiva con Python

---

## Fuentes de información

- **Delitos**: Estadísticas municipales del SESNSP (registros administrativos públicos)
- **Geografía**: Límites municipales del estado de Guanajuato
- **Población**: Estimaciones municipales utilizadas para el cálculo de tasas

> Por buenas prácticas y por el tamaño de los archivos, **los datos crudos y procesados no se incluyen en este repositorio**.  
> Todos los insumos provienen de fuentes públicas y pueden regenerarse localmente a partir de los scripts disponibles.

---

## Estructura del proyecto
- src/
 - revision_data.py
 - filtrado_homicidios.py
 - agregacion_municipal_anual.py
 - mapa_homicidios.py
- app.py # Aplicación en Streamlit
- requirements.txt
- README.md
- .gitignore

---

## Funcionalidades principales

- Filtrado de homicidios **dolosos y culposos**
- Cobertura temporal: **2020–2025**
- Agregación a nivel municipal
- Cálculo de **tasas por 100 mil habitantes**
- Mapa interactivo con:
  - Selección de año
  - Selección de subtipo de homicidio

---

## Ejecución local

1. Clonar el repositorio:
```bash
git clone https://github.com/MauricioAguilarOrta/sesnsp-guanajuato-homicidios.git
cd sesnsp-guanajuato-homicidios
```
2. (Opcional) Crear un entorno virtual

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:
```bash
streamlit run app.py
```

## Notas sobre reproducibilidad

- Este proyecto replica flujos de trabajo comunes en el análisis de políticas públicas y evaluación:
- Separación clara entre código y datos
- Uso de registros administrativos oficiales
- Procesos transparentes y reproducibles
- Énfasis en análisis territorial y contextualización de resultados

## Autor
Mauricio Aguilar