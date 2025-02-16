import yaml
import requests
from datetime import datetime

# https://developer.nutritionix.com/admin
# https://docs.google.com/spreadsheets/d/11ldogc7y-a_oar_-Mnsynr-O1-aIT_wJ9Aeyr8ooyns/edit?gid=0#gid=0

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 176
AGE = 25

APP_ID = config['APP_ID']
API_KEY = config['API_KEY']
SHEETY_TOKEN = config['SHEETY_TOKEN']


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/3336933bf23a9a760f0bd6357f04c82a/myWorkoutsPython/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        headers=bearer_headers
    )

    print(sheet_response.text)