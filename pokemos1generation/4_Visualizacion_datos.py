import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cargar_and_filtrar_csv import (
    cargar_y_filtrar_pokemon,
)  # Ajusta según el nombre de tu archivo


def visualizacion_datos():
    # cargar dataframe filtrado
    datos_pokemon = cargar_y_filtrar_pokemon()
    if datos_pokemon is None or datos_pokemon.empty:
        print("No se cargaron datos de Pokémon.")
        return None

    print("Ejercicio 4: Visualización de Datos")

    # 1. Histograma de Ataque
    plt.figure(figsize=(8, 6))
    sns.histplot(datos_pokemon["Ataque"], bins=15, kde=True, color="orange")
    plt.title("Histograma de Ataque")
    plt.xlabel("Valor de Ataque")
    plt.ylabel("Frecuencia")
    plt.show()

    # 2. Gráfico de dispersión Ataque vs Velocidad
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x="Ataque",
        y="Velocidad",
        data=datos_pokemon,
        hue="tipo_1",
        palette="Set2",
        s=100,
        edgecolor="k",
    )
    plt.title("Ataque vs Velocidad por Tipo Principal")
    plt.xlabel("Ataque")
    plt.ylabel("Velocidad")
    plt.legend(title="Tipo 1", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.show()

    # 3. Boxplot de PS por Tipo Principal
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="tipo_1", y="PS", data=datos_pokemon, palette="pastel")
    plt.title("Distribución de PS por Tipo Principal")
    plt.xlabel("Tipo 1")
    plt.ylabel("PS")
    plt.xticks(rotation=45)
    plt.show()

    # 4. Violín plot de Defensa por Tipo Principal
    plt.figure(figsize=(10, 6))
    sns.violinplot(
        x="tipo_1", y="Defensa", data=datos_pokemon, palette="muted", inner="quartile"
    )
    plt.title("Distribución de Defensa por Tipo Principal")
    plt.xlabel("Tipo 1")
    plt.ylabel("Defensa")
    plt.xticks(rotation=45)
    plt.show()


# ejecutar directamente al correr este archivo
visualizacion_datos()
