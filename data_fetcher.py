import os
import requests


API_KEY = os.getenv("API_NINJAS_KEY")
URL = "https://api.api-ninjas.com/v1/animals"


class DataFetchError(Exception):
    """Raised when animal data cannot be fetched."""


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns a list of animals, each animal represented by a dictionary.
    """

    if not API_KEY:
        raise RuntimeError("API key is missing.")

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    try:
        response = requests.get(
            URL,
            headers=headers,
            params=params
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        raise DataFetchError from error
