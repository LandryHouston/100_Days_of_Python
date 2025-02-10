import pandas as pd
import datetime as dt
import random
import yaml
import smtplib
import os
from email.message import EmailMessage

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

PASSWORD = config["password"]
EMAIL = config["email"]

image_path = "HappyBirthday.jpg"

birthdays = pd.read_csv('birthdays.csv')

current_month = dt.datetime.now().month
current_day= dt.datetime.now().day

for index, row in birthdays.iterrows():
    if row['Month'] == current_month and row['Day'] == current_day:
        templates = [file for file in os.listdir('letter_templates/')]
        with open(f'letter_templates/{random.choice(templates)}', 'r') as file:
            # Create email
            msg = EmailMessage()
            msg['Subject'] = "Happy Birthday!"
            msg['From'] = EMAIL
            msg['To'] = row.Email
            msg.set_content(file.read().replace("[NAME]", row.Name))
            # Attach image
            with open(image_path, 'rb') as img:
                msg.add_attachment(img.read(), maintype='image', subtype=os.path.splitext(image_path)[1][1:], filename=os.path.basename(image_path))
            # Send email
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.send_message(msg)