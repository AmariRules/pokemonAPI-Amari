# example_usage.py

from poke_sdk.PokeAPI import PokeAPI

def main():
    # Create an instance of the PokeAPI class
    api = PokeAPI()

    # Fetch a Pokémon by name
    try:
        pikachu = api.get_pokemon("pikachu")
        print(f"Retrieved Pokémon: {pikachu.name}")
        print(f"ID: {pikachu.id}")
        print(f"Types: {', '.join(pikachu.types)}")
    except Exception as e:
        print(f"An error occurred while fetching Pokémon: {e}")

    # Fetch a generation by ID
    try:
        generation = api.get_generation("1")
        print(f"Retrieved Generation: {generation.name}")
        print(f"ID: {generation.id}")
        print(f"Pokémon Species in this Generation: {', '.join(generation.pokemon_species)}")
    except Exception as e:
        print(f"An error occurred while fetching generation: {e}")
#new main
if __name__ == "__main__":
    main()
