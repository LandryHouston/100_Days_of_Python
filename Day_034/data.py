import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]