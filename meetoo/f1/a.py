import requests
import pandas as pd
from bs4 import BeautifulSoup

# Load HTML file
with open("amazon.html", "r", encoding="utf-8") as f:
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
    
    reviews.append({
        'user_name': user_name,
        'review_description': review_text,
        'rating': rating,
        'review_date': date
    })

# Create a DataFrame
df = pd.DataFrame(reviews)

# Save to CSV file
df.to_csv("amazon_reviews_tablet.csv", index=False)


