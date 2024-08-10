import pandas as pd
from bs4 import BeautifulSoup

# Load HTML file
with open("icloud_1.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

# Find all review sections
review_sections = soup.find_all('div', {'data-testid': 'review-card'})

reviews = []
for section in review_sections:
    user_name_tag = section.find('div', {'data-testid': 'reviewer-full-name'})
    user_name = user_name_tag.text.strip() if user_name_tag else 'N/A'
    
    overall_rating_tag = section.find('div', {'data-testid': 'Overall Rating-rating'})
    overall_rating = overall_rating_tag.find('span', {'class': 'text-neutral-80'}).text.strip() if overall_rating_tag else 'N/A'
    
    ease_of_use_tag = section.find('div', {'data-testid': 'Ease of Use-rating'})
    ease_of_use_rating = ease_of_use_tag.find('span', {'class': 'text-neutral-80'}).text.strip() if ease_of_use_tag else 'N/A'
    
    features_tag = section.find('div', {'data-testid': 'Features-rating'})
    features_rating = features_tag.find('span', {'class': 'text-neutral-80'}).text.strip() if features_tag else 'N/A'
    
    likelihood_to_recommend_tag = section.find('div', {'data-testid': 'Likelihood to Recommend-rating'})
    likelihood_to_recommend_rating = likelihood_to_recommend_tag.find_next('span', {'class': 'text-md'}).text.split('/')[0].strip() if likelihood_to_recommend_tag else 'N/A'
    
    review_content_tag = section.find('div', {'data-testid': 'review-content'})
    review_content = review_content_tag.text.strip() if review_content_tag else 'N/A'
    
    review_date_tag = section.find('div', {'data-testid': 'review-written-on'})
    review_date = review_date_tag.text.strip() if review_date_tag else 'N/A'

    reviews.append({
        'user_name': user_name,
        'overall_rating': overall_rating,
        'ease_of_use_rating': ease_of_use_rating,
        'features_rating': features_rating,
        'likelihood_to_recommend_rating': likelihood_to_recommend_rating,
        'review_text': review_content,
        'review_date': review_date
    })

# Create a DataFrame
df = pd.DataFrame(reviews)

# Save to CSV file
df.to_csv("icloud_reviews.csv", index=False)

# print(df)
