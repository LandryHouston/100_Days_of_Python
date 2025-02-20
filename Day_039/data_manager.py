import yaml
import requests

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/3336933bf23a9a760f0bd6357f04c82a/flightDealsPython/prices"
SHEETY_TOKEN = config['SHEETY_TOKEN']

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.bearer_headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
            }

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.bearer_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.bearer_headers
            )
            print(response.text)