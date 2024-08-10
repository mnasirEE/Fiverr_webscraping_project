from google_play_scraper import reviews, Sort
import pandas as pd

# Define the Google Play Store app ID
app_id = "com.dropbox.android"  # Change this to the app ID you want to scrape

# Define the number of reviews to fetch per batch and the total desired number of reviews
batch_size = 100  # Number of reviews per batch
total_reviews = 89700  # 10% of 897K
all_reviews = []

# Fetch reviews in batches
continuation_token = None
while len(all_reviews) < total_reviews:
    print(f"Fetching reviews for {len(all_reviews)} out of {total_reviews}")
    reviews_batch, continuation_token = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=batch_size,
        filter_score_with=None,
        continuation_token=continuation_token
    )
    
    # If no reviews are returned, break the loop
    if not reviews_batch:
        print("No more reviews found.")
        break
    
    # Extend the list of all reviews
    all_reviews.extend(reviews_batch)

# Convert the reviews into a DataFrame
reviews_df = pd.DataFrame(all_reviews)

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
reviews_df.to_csv('gplay_amazon_reviews.csv', index=False)

# Print the first few rows of the DataFrame
print(reviews_df.head())

# Print the number of reviews fetched
print(f"Total number of reviews fetched: {len(reviews_df)}")
