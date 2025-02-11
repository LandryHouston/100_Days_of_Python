import requests
import smtplib
import yaml
import os
import time
from datetime import datetime
from email.message import EmailMessage

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

PASSWORD = config["password"]
EMAIL = config["email"]
MY_LAT = 36.169941
MY_LONG = -115.139832

image_path = 'SpaceStation.jpg'

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data = iss_response.json()["iss_position"]
iss_longitude, iss_latitude = float(iss_data['longitude']), float(iss_data['latitude'])

def is_iss_overhead():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted":0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()['results']

    sunrise = int(data['sunrise'].split("T")[1].split(":")[0]) # Get Sunrise Hour
    sunset = int(data['sunset'].split("T")[1].split(":")[0]) # Get Sunset Hour

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        msg = EmailMessage()
        msg['Subject'] = "LOOK UP👆"
        msg['From'] = EMAIL
        msg['To'] = EMAIL
        msg.set_content("The ISS Space Station is flying over you!")
        # Attach image
        with open(image_path, 'rb') as img:
            msg.add_attachment(img.read(), maintype='image', subtype=os.path.splitext(image_path)[1][1:], filename=os.path.basename(image_path))
        # Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.send_message(msg)