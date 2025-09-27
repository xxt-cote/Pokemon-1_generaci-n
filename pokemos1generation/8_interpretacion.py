from cargar_and_filtrar_csv import cargar_y_filtrar_pokemon


def interpretacion_resultados():
    # cargar dataframe filtrado
    datos_pokemon = cargar_y_filtrar_pokemon()
    if datos_pokemon is None or datos_pokemon.empty:
        print("No se cargaron datos de Pokémon.")
        return None

    print("\nEjercicio 8: Interpretación de Resultados \n")

    print(
        "1. Los Pokémon de tipo 'psíquico' y 'dragón' tienden a tener estadísticas altas en ataque y defensa,"
    )
    print("   lo que los hace fuertes y resistentes en promedio.\n")

    print(
        "2. Existe una correlación positiva entre ataque y velocidad, lo que indica que los Pokémon más rápidos"
    )
    print(
        "   suelen ser también más ofensivos, aunque no siempre es estrictamente así.\n"
    )

    print("3. Tipos como 'normal' o 'agua' muestran gran dispersión en PS,")
    print(
        "   es decir, dentro de un mismo tipo hay Pokémon muy resistentes y otros más frágiles.\n"
    )

    print("4. Los boxplots de ataque y PS revelan algunos valores atípicos (outliers),")
    print(
        "   por ejemplo, Chansey con PS extremadamente altos y Mewtwo con ataques fuera de lo común.\n"
    )

    print(
        "5. En general, un Pokémon 'balanceado' posee valores medianos en todas las estadísticas,"
    )
    print(
        "   como Venusaur o Blastoise, mientras que un 'especializado' destaca en un atributo específico,"
    )
    print(" por ejemplo, Chansey en PS o Alakazam en velocidad y ataque especial.\n")

    print(
        "Conclusión: Los datos de la primera generación muestran que la fortaleza o especialización"
    )
    print("de cada Pokémon depende de su tipo y su rol en combate.\n")


# ejecutar al correr este archivo
interpretacion_resultados()
