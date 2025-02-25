import yaml
import requests
import smtplib
from bs4 import BeautifulSoup

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

PASSWORD = config["password"]
EMAIL = config["email"]

urls = {"https://www.amazon.com/gp/product/B01LZAM6TR/ref=ox_sc_saved_image_9?smid=ATVPDKIKX0DER&th=1":270,
        "https://www.amazon.com/gp/product/B06XDSQDBV/ref=ox_sc_saved_image_1?smid=ATVPDKIKX0DER&psc=1":280,
        "https://www.amazon.com/gp/product/B0BZK2Z2TC/ref=ox_sc_saved_image_4?smid=ATVPDKIKX0DER&th=1":130,
        "https://www.amazon.com/gp/product/B0B2QXF7KW/ref=ox_sc_saved_image_1?smid=A3DJTZRS1C5A82&th=1":30,
        "https://www.amazon.com/gp/product/B002VUAM46/ref=ox_sc_act_image_3?smid=ATVPDKIKX0DER&psc=1":10
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
}


for url, list_price in urls.items():
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find('h1', id='title').text
    title = ' '.join(title.split())

    price = soup.find("span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").text
    price_without_currency = price.replace('$','').strip()
    price_as_float = float(price_without_currency)

    if price_as_float < list_price:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{title} is now ${price_as_float}.".encode('utf-8')
            )