import yaml
import requests

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_API_KEY = config["AMADEUS_API_KEY"]
AMADEUS_SECRET = config['AMADEUS_SECRET']
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:

    def __init__(self):
        self._token = self._get_new_token()

    def get_destination_code(self, city_name):
        print(f"Getting destination code for {city_name} using token {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "subType": "AIRPORT",
            "page[limit]": "2",  # Use the correct pagination parameter
        }
        response = requests.get(
            url="https://test.api.amadeus.com/v1/reference-data/locations",
            headers=headers,
            params=query
        )

        print(f"Status code {response.status_code}. Response: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except (IndexError, KeyError):
            print(f"No airport code found for {city_name}.")
            return "Not Found"
        return code


    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': AMADEUS_API_KEY,
            'client_secret': AMADEUS_SECRET
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
