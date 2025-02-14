import yaml
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

NEWS_API_KEY = config["NEWS_API_KEY"]
ALPHAVANTAGE_API_KEY = config["ALPHAVANTAGE_API_KEY"]
twilio_account_sid = config["twilio_account_sid"]
twilio_auth_token = config["twilio_auth_token"]
twilio_messaging_service_sid = config["twilio_messaging_service_sid"]
phone_number = config["phone_number"]

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

client = Client(twilio_account_sid, twilio_auth_token)

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

news_params = {
    'q': COMPANY_NAME,
    'from': (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d'),
    'sortBy': 'popularity',
    'apiKey': NEWS_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, stock_params)
stock_data = stock_response.json()['Time Series (Daily)']

news_response = requests.get(NEWS_ENDPOINT, news_params)
news_data = news_response.json()['articles']
three_articles = news_data[:3]

yesterday = float(stock_data[(datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')]['4. close'])
day_before_yesterday = float(stock_data[(datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')]['4. close'])

percentage_change = ((yesterday - day_before_yesterday) / day_before_yesterday) * 100

up_down = "🔺" if percentage_change > 0 else "🔻"

formatted_articles = [
    f"{STOCK}: {up_down}{round(percentage_change)}%\nHeadline: {article['title']}\nBrief: {article['description']}\nRead More: {article['url']}"
    for article in three_articles
]
if abs(percentage_change) > 5:
    for article in formatted_articles:
        message = client.messages.create(
            messaging_service_sid=twilio_messaging_service_sid,
            body=article,
            to=f'+1{phone_number}'
        )
    print("Message Sent")