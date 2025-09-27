import pandas as pd
from cargar_and_filtrar_csv import cargar_pokemons


def obtener_pokemon_fuego():
    df = cargar_pokemons("pokemon_primera_gen.csv")
    pokemons_fuego = df[df["tipo_1"] == "fuego"]
    pokemons_fuego = pokemons_fuego[["Nombre", "tipo_1", "Ataque", "Velocidad"]]

    print("=====================================")
    print("Pokémons de tipo fuego")
    print("Cantidad de pokémons tipo fuego:", len(pokemons_fuego))
    print(pokemons_fuego)
    return pokemons_fuego


if __name__ == "__main__":
    obtener_pokemon_fuego()
