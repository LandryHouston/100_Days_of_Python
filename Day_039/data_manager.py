import yaml
import requests

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

SHEETY_TOKEN = config['SHEETY_TOKEN']
sheet_endpoint = "https://api.sheety.co/3336933bf23a9a760f0bd6357f04c82a/flightDealsPython/prices"
bearer_headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_endpoint, headers=bearer_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{sheet_endpoint}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )
            print(response.text)
