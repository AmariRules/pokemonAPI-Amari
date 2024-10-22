import unittest
from poke_sdk.PokeAPI import PokeAPI
from poke_sdk.exceptions import APIError


class InteractiveTestPokeAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the API client for testing."""
        cls.api = PokeAPI()

    def test_get_pokemon_with_user_input(self):
        """Test retrieving a Pokémon based on user input. Will return Pokémon Type and generation"""
        pokemon_name = input("Enter the Pokémon name (e.g., pikachu, charizard, blastoise): ")
        try:
            response = self.api.get_pokemon(pokemon_name)
            print(f"Retrieved Pokémon: {response.name}, ID: {response.id}, Types: {response.types}")
            self.assertEqual(response.name, pokemon_name)
        except APIError as e:
            self.fail(f"APIError occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def test_get_pokemon_in_generation(self):
        """Test retrieving Pokémon in a specified generation based on user input. Returns all Pokémon in generation"""
        generation_id = input("Enter the generation ID (e.g., 1): ")
        try:
            response = self.api.get_generation(generation_id)
            print(f"Retrieved Generation: {response.name}, ID: {response.id}")
            print("Pokémon in this generation:")
            for pokemon in response.pokemon_species:
                print(f"- {pokemon}")
        except APIError as e:
            self.fail(f"APIError occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    #Test generation is a valid Pokémon Generation based on user input
    def test_get_generation_with_user_input(self):
        """Test retrieving a generation based on user input. Will validate Pokémon generation is a valid Gen"""
        generation_id = input("Enter the generation ID, will validate if gen is available(e.g., 1): ")
        try:
            response = self.api.get_generation(generation_id)
            print(f"Retrieved Generation: {response.name}, ID: {response.id}")
            self.assertEqual(response.id, int(generation_id))
        except APIError as e:
            self.fail(f"APIError occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    unittest.main()
