import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cargar_and_filtrar_csv import cargar_y_filtrar_pokemon


def analisis_exploratorio():
    # cargar dataframe filtrado
    datos_pokemon = cargar_y_filtrar_pokemon()
    if datos_pokemon is None or datos_pokemon.empty:
        print("No se cargaron datos de Pokémon.")
        return None

    print("\nEjercicio 7: Análisis Exploratorio (EDA)\n")

    # 1. Promedio de ataque y defensa por tipo
    ataque_defensa = (
        datos_pokemon.groupby("tipo_1")[["Ataque", "Defensa"]].mean().round(2)
    )
    ataque_defensa = ataque_defensa.sort_values(by="Ataque", ascending=False)
    print("Promedio de ataque y defensa por tipo principal:")
    print(ataque_defensa, "\n")

    # 2. Correlación entre ataque y velocidad
    correlacion = datos_pokemon["Ataque"].corr(datos_pokemon["Velocidad"])
    print(f"Correlación entre ataque y velocidad: {correlacion:.2f}\n")

    # 3. Dispersión de PS por tipo (desviación estándar)
    dispersion_ps = (
        datos_pokemon.groupby("tipo_1")["PS"]
        .std()
        .round(2)
        .sort_values(ascending=False)
    )
    print("Dispersión de PS por tipo (desviación estándar):")
    print(dispersion_ps, "\n")

    # 4. Boxplots para identificar outliers
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=datos_pokemon["Ataque"])
    plt.title("Boxplot de Ataque (identificación de outliers)")
    plt.xlabel("Ataque")
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.boxplot(x=datos_pokemon["PS"])
    plt.title("Boxplot de PS (identificación de outliers)")
    plt.xlabel("PS")
    plt.show()

    return {
        "ataque_defensa": ataque_defensa,
        "correlacion": round(correlacion, 2),
        "dispersion_ps": dispersion_ps,
    }


# ejecutar al correr este archivo
analisis_exploratorio()
