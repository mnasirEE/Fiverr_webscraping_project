import requests
from bs4 import BeautifulSoup

def fetch_data(path, url):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://play.google.com/store/apps/details?id=com.amazon.clouddrive.photos&hl=en_US&gl=US"
fetch_data("amazon_photos.html", url)

with open("amazon_photos.html", "r", encoding="utf-8") as f:  # Corrected file name
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
div_h3YV2d = soup.find_all('div', {'class': "h3YV2d"})

reviews = []
for div in div_h3YV2d:
    reviews.append(div.text)

print(reviews)
