import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18 # Science: Computers
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
results = response.json()['results']

question_data = [question for question in response.json()['results']]