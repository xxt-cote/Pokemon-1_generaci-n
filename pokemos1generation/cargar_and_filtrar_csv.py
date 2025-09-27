import pandas as pd
import unicodedata


# --- Función para normalizar texto: minúsculas, sin tildes, sin espacios ---
def normalizar_tipo(tipo_pokemon):
    if pd.isna(tipo_pokemon):
        return None
    texto = str(tipo_pokemon).strip().lower()
    texto_sin_tildes = "".join(
        c
        for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )
    return texto_sin_tildes


# --- Función para cargar y filtrar Pokémon ---
def cargar_y_filtrar_pokemon(ruta_csv="pokemon_primera_gen.csv"):
    # Cargar CSV
    df = pd.read_csv(ruta_csv, sep=";")  # Ajusta sep si tu CSV usa otro separador
    df.columns = (
        df.columns.str.strip()
    )  # Eliminar espacios extra en nombres de columnas

    # Normalizar columnas de tipo
    df["tipo_1"] = df["Tipo 1"].apply(normalizar_tipo)
    df["tipo_2"] = df["Tipo 2"].apply(normalizar_tipo)

    # Tipos válidos de primera generación
    tipos_validos_gen1 = {
        "planta",
        "fuego",
        "agua",
        "bicho",
        "normal",
        "veneno",
        "tierra",
        "volador",
        "psiquico",
        "electrico",
        "hielo",
        "roca",
        "lucha",
        "fantasma",
        "dragon",
    }

    # Filtrar Pokémon
    df_filtrado = df[
        df["tipo_1"].isin(tipos_validos_gen1)
        & (df["tipo_2"].isna() | df["tipo_2"].isin(tipos_validos_gen1))
    ].copy()

    return df_filtrado


# --- Código de prueba ---
if __name__ == "__main__":
    df_filtrado = cargar_y_filtrar_pokemon()
    print("Primeras filas del dataframe filtrado:")
    print(df_filtrado.head())
    print(f"\nCantidad de Pokémon después del filtrado: {len(df_filtrado)}")
