import yaml
import requests
from datetime import datetime, timedelta

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

TOKEN = config['TOKEN']
USERNAME = "landryhouston"
GRAPHID = 'codinggraph'

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
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# https://pixe.la/v1/users/landryhouston/graphs/codinggraph.html

value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

value_config = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": '120'
}

# response = requests.post(url=value_endpoint, json=value_config, headers=headers)
# print(response.text)