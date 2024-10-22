import unittest
from poke_sdk.PokeAPI import PokeAPI
from poke_sdk.exceptions import APIError


class TestPokeAPI(unittest.TestCase):

    def setUp(self):
        self.api = PokeAPI()

    def test_get_pokemon_valid(self):
        response = self.api.get_pokemon("pikachu")
        self.assertEqual(response.name, 'pikachu')
        self.assertEqual(response.id, 25)

    def test_get_pokemon_invalid(self):
        with self.assertRaises(APIError):
            self.api.get_pokemon("invalid_name")

    def test_get_generation_valid(self):
        response = self.api.get_generation("1")
        self.assertEqual(response.id, 1)
        self.assertEqual(response.name, 'generation-i')

    def test_get_generation_invalid(self):
        with self.assertRaises(APIError):
            self.api.get_generation("invalid_id")


if __name__ == '__main__':
    unittest.main()
