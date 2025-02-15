import yaml
import requests

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

TOKEN = config['TOKEN']
USERNAME = "landryhouston"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# https://pixe.la/@landryhouston

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "codinggraph",
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
# https://pixe.la/v1/users/landryhouston/graphs/codinggraph.html