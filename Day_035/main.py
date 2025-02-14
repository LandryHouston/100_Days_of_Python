import yaml
import requests
from twilio.rest import Client

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

OWM_API_KEY = config["OWM_API_KEY"]
twilio_account_sid = config["twilio_account_sid"]
twilio_auth_token = config["twilio_auth_token"]
twilio_messaging_service_sid = config["twilio_messaging_service_sid"]
phone_number = config["phone_number"]

zipcode = "89113"

parameters = {
    "zip": zipcode,
    "appid": OWM_API_KEY,
    "cnt": 4
}

owm_response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
owm_response.raise_for_status()
weather_data = owm_response.json()

sent_message = False

for i in range(parameters['cnt']):
    if int(weather_data['list'][i]['weather'][0]['id']) < 700 and not sent_message:
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            messaging_service_sid=twilio_messaging_service_sid,
            body="Good Morning! It's going to rain today. Remember to bring a jacket!",
            to=f'+1{phone_number}'
        )
        sent_message = True
        break