import requests
from .exceptions import APIError


class APIClient:
    BASE_URL = "https://pokeapi.co/api/v2"

    def __init__(self):
        pass

    def get(self, endpoint):
        """Send a GET request to the specified endpoint."""
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url)

        if response.status_code != 200:
            raise APIError(f"Error fetching data: {response.status_code} - {response.text}")

        return response.json()
