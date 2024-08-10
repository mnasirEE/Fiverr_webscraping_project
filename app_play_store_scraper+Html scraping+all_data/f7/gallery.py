import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

# Initialize the AppStore scraper
gallery = AppStore(country='us', app_name='gallery-photo-vault', app_id='1450715436')

# Fetch reviews
gallery.review(how_many=350)

# Create a DataFrame from the reviews
df = pd.DataFrame(np.array(gallery.reviews), columns=['review'])
slackdf2 = df.join(pd.DataFrame(df.pop('review').tolist()))

# Display the first few rows of the DataFrame

# Append the data to the existing CSV file without overwriting
slackdf2.to_csv('gallery_reviews_us2.csv', mode='a', index=False, header=False)

# # Create a DataFrame
# df = pd.DataFrame({'amazon_photos_reviews': gallery})

# # Save to Excel file
# df.to_excel("amazon_photos_3.xlsx", index=False)
