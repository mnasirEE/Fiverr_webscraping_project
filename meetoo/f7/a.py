import requests
import pandas as pd
from bs4 import BeautifulSoup

# Load HTML file
with open("a.html", "r", encoding="utf-8") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')

# Extract review sections
review_sections = soup.find_all('div', {'class': 'RHo1pe'})

reviews = []

for section in review_sections:
    # Extract user name
    user_name_tag = section.find('div', {'class': 'X5PpBb'})
    user_name = user_name_tag.text if user_name_tag else 'N/A'
    
    # Extract rating
    rating_div = section.find('div', {'role': 'img'})
    if rating_div and 'aria-label' in rating_div.attrs:
        try:
            rating = int(rating_div['aria-label'].split(' ')[1])
        except (IndexError, ValueError):
            rating = 'N/A'
    else:
        rating = 'N/A'
    
    # Extract date
    date_tag = section.find('span', {'class': 'bp9Aid'})
    date = date_tag.text if date_tag else 'N/A'
    
    # Extract review text
    review_text_tag = section.find('div', {'class': 'h3YV2d'})
    review_text = review_text_tag.text if review_text_tag else 'N/A'
    a = len(date)
    # ise = []
    # t= []
    # dr = []
    # for i in range(a):
    #     if son == 1:
    #         ise.append()
    #         t.append()
    #         dr.append()
    # son = 0    

    reviews.append({
        'date': date,
        'review': review_text,
        'rating': rating,
        'isEdited': '',
        'title':'', 
        'userName': user_name,
        'developerResponce':''

    })

# Create a DataFrame
df = pd.DataFrame(reviews)

# Save to CSV file
df.to_csv("gallery_google_play.csv", index=False)


