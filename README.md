# Análisis de datos: Pokémon primera generación

Serie de ejercicios de análisis de datos con pandas/seaborn/matplotlib sobre un dataset
de Pokémon de primera generación (`pokemon_primera_gen.csv`).

## Estructura

Todos los scripts se ejecutan desde la carpeta `pokemos1generation/`:

- `cargar_and_filtrar_csv.py`: carga y normaliza el CSV, filtra tipos válidos de 1ª gen.
- `2_filtrar_tipo.py`: filtra Pokémon de tipo fuego.
- `3_estadistica_description.py`: estadísticas descriptivas (media, mediana, moda, etc.).
- `4_Visualizacion_datos.py`: histogramas, dispersión, boxplots y violin plots.
- `5_manipulacion_datos.py`: cálculo de "Poder_Total" y ordenamiento.
- `6_agrup_analisisporgrup.py`: agrupamientos y análisis por tipo.
- `7_analisis_explot.py`: análisis exploratorio (correlaciones, outliers).
- `8_interpretacion.py`: interpretación de resultados.

## Uso

```bash
pip install pandas seaborn matplotlib
cd pokemos1generation
python 3_estadistica_description.py   # por ejemplo
```
