# Import packages
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# Header to set the requests as a browser requests
headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

# URL of The amazon Review page
reviews_url = 'https://www.amazon.com/Amazon-com-Amazon-Photos/dp/B00A11AN6O'

# Define Page No
len_page = 250

### Functions

# Extra Data as Html object from amazon Review page
def reviewsHtml(url, len_page):
    
    # Empty List define to store all pages html data
    soups = []
    
    # Loop for gather all reviews from pages via range
    for page_no in range(1, len_page + 1):
        
        # parameter set as page no to the requests body
        params = {
            'ie': 'UTF8',
            'reviewerType': 'all_reviews',
            'filterByStar': 'critical',
            'pageNumber': page_no,
        }
        
        # Request make for each page
        response = requests.get(url, headers=headers, params=params)
        
        # Save Html object by using BeautifulSoup4 and lxml parser
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Add single Html page data in master soups list
        soups.append(soup)
        
    return soups

# Grab Reviews name, description, date, stars, title from HTML
def getReviews(html_data):

    # Create Empty list to Hold all data
    data_dicts = []
    
    # Select all Reviews BOX html using css selector
    boxes = html_data.select('div[data-hook="review"]')
    
    # Iterate all Reviews BOX 
    for box in boxes:
        
        # Select Name using css selector and cleaning text using strip()
        # If Value is empty define value with 'N/A' for all.
        try:
            name = box.select_one('[class="a-profile-name"]').text.strip()
        except Exception as e:
            name = 'N/A'

        try:
            stars = box.select_one('[data-hook="review-star-rating"]').text.strip().split(' out')[0]
        except Exception as e:
            stars = 'N/A'   

        try:
            title = box.select_one('[data-hook="review-title"]').text.strip()
        except Exception as e:
            title = 'N/A'

        try:
            # Extract and clean the date string
            datetime_str = box.select_one('[data-hook="review-date"]').text.strip().split(' on ')[-1]
            # print("Extracted datetime string:", datetime_str)  # Debug print

            # Convert date str to dd/mm/yyyy format
            date = datetime.strptime(datetime_str, '%B %d, %Y').strftime("%d/%m/%Y")
            # print("Formatted date:", date)  # Debug print
        except Exception as e:
            date = 'N/A'
            # print("Error:", e)  # Debug print

        try:
            description = box.select_one('[data-hook="review-body"]').text.strip()
        except Exception as e:
            description = 'N/A'

        # Create Dictionary with all review data 
        data_dict = {
            'Name' : name,
            'Stars' : stars,
            'Title' : title,
            'Date' : date,
            'Description' : description
        }

        # Add Dictionary in master empty List
        data_dicts.append(data_dict)
    
    return data_dicts

### Data Process

# Grab all HTML
html_datas = reviewsHtml(reviews_url, len_page)

# Empty List to Hold all reviews data
reviews = []

# Iterate all Html pages 
for html_data in html_datas:
    
    # Grab review data
    review = getReviews(html_data)
    
    # Add review data in reviews empty list
    reviews += review

# Create a dataframe with reviews Data
df_reviews = pd.DataFrame(reviews)

# Save data
df_reviews.to_csv('amazon_photos_OnAmazon1.csv', index=False)
