import requests
from config import POKE_API_URL


def fetch_berry_details(berry_id):
    """
    api request to fetch pokemon berry details
    """
    try:
        url = f"{POKE_API_URL}/{berry_id}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None

def fetch_all_berry_data():
    """
    fetch all pokemon berry data
    """
    berries = []
    for i in range(1, 65):
        berry = fetch_berry_details(i)
        if berry:
            berries.append(berry)
    return berries
