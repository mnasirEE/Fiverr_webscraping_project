import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore
gallery = AppStore(country='gb', app_name='microsoft-onedrive', app_id = '477537958')

gallery.review(how_many=45100)


df = pd.DataFrame(np.array(gallery.reviews),columns=['review'])
slackdf2 = df.join(pd.DataFrame(df.pop('review').tolist()))
slackdf2.head()
slackdf2.to_csv('onedrive-reviews_gb1.csv')
# # Create a DataFrame
# df = pd.DataFrame({'amazon_photos_reviews': gallery})

# # Save to Excel file
# df.to_excel("amazon_photos_3.xlsx", index=False)