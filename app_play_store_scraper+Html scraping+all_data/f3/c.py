import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore
gallery = AppStore(country='us', app_name='gallery-photo-vault', app_id='1450715436')

gallery.review(how_many=2000)


df = pd.DataFrame(np.array(gallery.reviews),columns=['review'])
slackdf2 = df.join(pd.DataFrame(df.pop('review').tolist()))
slackdf2.head()
slackdf2.to_csv('gallery_reviews.csv')
# # Create a DataFrame
# df = pd.DataFrame({'amazon_photos_reviews': gallery})

# # Save to Excel file
# df.to_excel("amazon_photos_3.xlsx", index=False)