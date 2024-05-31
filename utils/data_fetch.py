import requests
from config import POKE_API_URL

def fetch_poke_berry_data():
    """
    api request to fetch pokemon berry data
    """
    try:
        response = requests.get(POKE_API_URL, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as e:
        print(f"Error fetchingPokemon Berry data: {e}")
        return None
