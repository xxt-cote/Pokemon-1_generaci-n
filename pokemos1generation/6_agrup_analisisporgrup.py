import pandas as pd
from cargar_and_filtrar_csv import cargar_y_filtrar_pokemon


def agrupamiento_por_tipo():
    # cargar dataframe filtrado
    datos_pokemon = cargar_y_filtrar_pokemon()
    if datos_pokemon is None or datos_pokemon.empty:
        print("No se cargaron datos de Pokémon.")
        return None

    print("\nEjercicio 6: Agrupamiento y Análisis por Tipo\n")

    # 1. Promedio, mediana y desviación estándar de ataque por tipo principal
    ataque_stats = (
        datos_pokemon.groupby("tipo_1")["Ataque"]
        .agg(["mean", "median", "std"])
        .round(2)
    )
    print("Promedio, mediana y desviación estándar de ataque por tipo principal:")
    print(ataque_stats, "\n")

    # 2. Tipo con mayor promedio de velocidad
    velocidad_promedio = datos_pokemon.groupby("tipo_1")["Velocidad"].mean()
    tipo_mas_rapido = velocidad_promedio.idxmax()
    valor_mas_rapido = velocidad_promedio.max()
    print(
        f"Tipo con mayor promedio de velocidad: {tipo_mas_rapido} ({valor_mas_rapido:.2f})\n"
    )

    # 3. Pokémon con mayor y menor PS por tipo principal
    mayor_ps = datos_pokemon.loc[
        datos_pokemon.groupby("tipo_1")["PS"].idxmax(), ["tipo_1", "Nombre", "PS"]
    ].reset_index(drop=True)

    menor_ps = datos_pokemon.loc[
        datos_pokemon.groupby("tipo_1")["PS"].idxmin(), ["tipo_1", "Nombre", "PS"]
    ].reset_index(drop=True)

    print("Pokémon con mayor PS por tipo principal:")
    print(mayor_ps, "\n")

    print("Pokémon con menor PS por tipo principal:")
    print(menor_ps, "\n")

    return {
        "ataque_stats": ataque_stats,
        "tipo_mas_rapido": (tipo_mas_rapido, valor_mas_rapido),
        "mayor_ps": mayor_ps,
        "menor_ps": menor_ps,
    }


# ejecutar directamente al correr este archivo
agrupamiento_por_tipo()
