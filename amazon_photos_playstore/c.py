import requests
import pandas as pd
from bs4 import BeautifulSoup

with open("b.html", "r", encoding="utf-8") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')

# # Extract the review text
# review_text = soup.find('span', {'jsname': 'bN97Pc'}).text
# print(review_text)