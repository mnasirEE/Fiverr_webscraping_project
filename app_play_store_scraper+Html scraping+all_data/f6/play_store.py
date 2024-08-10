from google_play_scraper import Sort, reviews_all
import pandas as pd
import numpy as np

# Define the Google Play Store app ID
app_id = "com.amazon.clouddrive.photos"  # Example app ID for Dropbox

# Scrape all reviews for the specified app
reviews = reviews_all(
    app_id,
    sleep_milliseconds=0,  # Adjust sleep time if necessary
    lang='en',  # Language of the reviews
    country='us',  # Country of the reviews
    sort=Sort.NEWEST  # Sort order: NEWEST, RATING, HELP
)

# Convert the reviews into a DataFrame
reviews_df = pd.DataFrame(reviews)

# Display the columns to understand the structure of the DataFrame
print("Columns in the DataFrame:", reviews_df.columns)

# Select and rename the relevant columns
reviews_df = reviews_df[['reviewId', 'userName', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion', 'at', 'replyContent', 'repliedAt']]
reviews_df.rename(columns={
    'reviewId': 'review_id',
    'userName': 'user_name',
    'content': 'review_description',
    'score': 'rating',
    'thumbsUpCount': 'thumbs_up',
    'reviewCreatedVersion': 'review_version',
    'at': 'review_date',
    'replyContent': 'developer_response',
    'repliedAt': 'developer_response_date'
}, inplace=True)

# Add source, language_code, and country_code columns
reviews_df.insert(loc=0, column='source', value='Google Play')
reviews_df['language_code'] = 'en'
reviews_df['country_code'] = 'us'

# Save the DataFrame to a CSV file
reviews_df.to_csv('amazon_reviews_US.csv', index=False)

# Print the first few rows of the DataFrame
print(len(reviews_df))
