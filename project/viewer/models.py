from django.db import models
import requests
from requests.exceptions import HTTPError

# Create your models here.
class APIViewer:
    api_url = ""

    def __init__(self):
        self.api_url = "https://swapi.dev/api/people/"

    @property
    def fetch_name_height_mass(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            jsonResponse = response.json()

            result = jsonResponse['results']

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

        return result

