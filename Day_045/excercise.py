# See what you can scrape using /robots.txt
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all("tr", class_="athing")

article_texts = []
article_links = []
article_upvotes = []

for article in articles:
    title_tag = article.find("span", class_="titleline").find("a")
    if title_tag:
        article_texts.append(title_tag.getText())
        article_links.append(title_tag["href"])

    score_tag = article.find_next_sibling().find("span", class_="score")
    if score_tag:
        article_upvotes.append(int(score_tag.getText().split()[0]))
    else:
        article_upvotes.append(0)  # Assume 0 upvotes if not found

# Find the index of the article with the most upvotes
largest_index = article_upvotes.index(max(article_upvotes))

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])
