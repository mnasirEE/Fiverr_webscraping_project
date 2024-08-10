import pandas as pd
from app_store_scraper import AppStore

# Define countries you want to fetch reviews from
countries = ['us', 'gb']  # Add more countries as needed

# Initialize an empty list to store all reviews
all_reviews = []

for country in countries:
    # Initialize the AppStore object for each country
    gallery = AppStore(country=country, app_name='gallery-photo-vault', app_id='1450715436')
    
    # Fetch reviews in multiple requests until you get the desired number of reviews
    reviews = gallery.review(how_many=2000)
    
    # Check if any reviews are fetched
    if reviews:
        # Append reviews for the current country to the list of all reviews
        all_reviews.extend(reviews)
    else:
        print(f"No reviews found for {country}.")

# Convert the reviews into a DataFrame
df = pd.DataFrame(all_reviews)

# Save DataFrame to CSV
df.to_csv('Slack-app-reviews.csv', index=False)
