import pandas as pd
from cargar_and_filtrar_csv import (
    cargar_y_filtrar_pokemon,
)


def manipulacion_datos():
    # cargar dataframe filtrado
    datos_pokemon = cargar_y_filtrar_pokemon()
    if datos_pokemon is None or datos_pokemon.empty:
        print("No se cargaron datos de Pokémon.")
        return None

    print("\nEjercicio 5: Manipulación de Datos\n")

    # 1. Crear nueva columna "Poder_Total"
    datos_pokemon["Poder_Total"] = (
        datos_pokemon["Ataque"]
        + datos_pokemon["Defensa"]
        + datos_pokemon["Velocidad"]
        + datos_pokemon["PS"]
    )

    # 2. Ordenar DataFrame por "Poder_Total" de mayor a menor
    datos_ordenados = datos_pokemon.sort_values(by="Poder_Total", ascending=False)

    # 3. Mostrar las primeras 20 filas del DataFrame ordenado
    print("Pokémons ordenados por Poder_Total (top 20):")
    print(
        datos_ordenados[
            ["Nombre", "tipo_1", "Ataque", "Defensa", "Velocidad", "PS", "Poder_Total"]
        ].head(20)
    )

    return datos_ordenados


# ejecutar directamente al correr este archivo
manipulacion_datos()
