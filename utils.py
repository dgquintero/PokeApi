import requests
from config import POKE_API_URL

def fetch_pokemon_data():
    """
    api request to fetch pokemon data
    """
    response = requests.get(POKE_API_URL, timeout=5)

    if response.status_code == 200:
        return response.json()
    else:
        return None
