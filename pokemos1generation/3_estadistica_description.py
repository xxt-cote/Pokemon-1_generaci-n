from cargar_and_filtrar_csv import cargar_y_filtrar_pokemon
import pandas as pd


def estadisticas_pokemon():
    # Cargar los datos filtrados
    df = cargar_y_filtrar_pokemon()
    if df is None or df.empty:
        print("No se pudieron cargar los datos de Pokémon.")
        return None

    print("===================================")
    print("          ESTADÍSTICAS POKÉMON     ")
    print("===================================\n")

    # ---- 1. Estadísticos de ataque ----
    ataque_prom = df["Ataque"].mean()
    ataque_med = df["Ataque"].median()
    ataque_moda = df["Ataque"].mode()[0]

    print(f"Promedio de Ataque: {ataque_prom:.2f}")
    print(f"Mediana de Ataque: {ataque_med}")
    print(f"Moda de Ataque: {ataque_moda}\n")

    # ---- 2. Pokémon con mayor defensa ----
    idx_max_def = df["Defensa"].idxmax()
    max_def_pokemon = df.loc[idx_max_def, ["Nombre", "Defensa"]]
    print("Pokémon con mayor defensa:")
    print(max_def_pokemon.to_string(), "\n")  # to_string evita mostrar Name y dtype

    # ---- 3. Pokémon con menor velocidad ----
    idx_min_vel = df["Velocidad"].idxmin()
    min_vel_pokemon = df.loc[idx_min_vel, ["Nombre", "Velocidad"]]
    print("Pokémon con menor velocidad:")
    print(min_vel_pokemon.to_string(), "\n")

    # ---- 4. Conteo de Pokémon con doble tipo ----
    doble_tipo = df["tipo_2"].notna().sum()
    print(f"Cantidad de Pokémon con dos tipos: {doble_tipo}\n")

    # ---- 5. Rango y desviación estándar de PS ----
    ps_rango = df["PS"].max() - df["PS"].min()
    ps_desv = df["PS"].std()
    print(f"Rango de PS: {ps_rango}")
    print(f"Desviación estándar de PS: {ps_desv:.2f}")

    # Devolver resultados en un diccionario para uso posterior si se quiere
    return {
        "ataque_prom": ataque_prom,
        "ataque_med": ataque_med,
        "ataque_moda": ataque_moda,
        "max_def_pokemon": max_def_pokemon,
        "min_vel_pokemon": min_vel_pokemon,
        "doble_tipo": doble_tipo,
        "ps_rango": ps_rango,
        "ps_desv": ps_desv,
    }


# Ejecutar función si se corre este script directamente
if __name__ == "__main__":
    estadisticas_pokemon()
