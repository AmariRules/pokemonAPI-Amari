from .api_client import APIClient
from .models import Pokemon, Generation


class PokeAPI:
    def __init__(self):
        self.client = APIClient()

    def get_pokemon(self, identifier: str) -> Pokemon:
        """Fetches a Pokémon by its name or ID."""
        data = self.client.get(f"pokemon/{identifier}")
        return Pokemon(name=data['name'], id=data['id'], types=[t['type']['name'] for t in data['types']])

    def get_generation(self, identifier: str) -> Generation:
        """Fetches a generation by its ID or name."""
        data = self.client.get(f"generation/{identifier}")
        return Generation(id=data['id'], name=data['name'], pokemon_species=[ps['name'] for ps in data['pokemon_species']])
