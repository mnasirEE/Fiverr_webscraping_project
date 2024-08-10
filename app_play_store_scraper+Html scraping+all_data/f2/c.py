import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# Function to fetch HTML content
def fetch_html(url, params=None, headers=None):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Check for HTTP errors
    return BeautifulSoup(response.text, 'html.parser')

# Function to extract reviews from HTML
def extract_reviews(soup):
    reviews = []

    review_boxes = soup.select('div.we-customer-review')  # Apple App Store
    for box in review_boxes:
        try:
            name = box.select_one('.we-truncate').text.strip()
        except Exception:
            name = 'N/A'
        
        try:
            stars = box.select_one('figure span').text.strip()
        except Exception:
            stars = 'N/A'
        
        try:
            title = box.select_one('.we-customer-review__title').text.strip()
        except Exception:
            title = 'N/A'
        
        try:
            date_str = box.select_one('time').text.strip()
            date = datetime.strptime(date_str, '%B %d, %Y').strftime("%d/%m/%Y")
        except Exception:
            date = 'N/A'
        
        try:
            description = box.select_one('.we-customer-review__body').text.strip()
        except Exception:
            description = 'N/A'

        reviews.append({
            'Name': name,
            'Stars': stars,
            'Title': title,
            'Date': date,
            'Description': description
        })

    return reviews

# Function to save reviews to CSV
def save_reviews_to_csv(reviews, filename):
    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False)
    print(f"Reviews saved to {filename}")

# Function to scrape reviews from multiple pages
def scrape_app_store_reviews(url, headers=None, output_file='app_store_reviews.csv', max_pages=10):
    all_reviews = []
    
    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}")
        params = {
            'page': page
        }
        html = fetch_html(url, params=params, headers=headers)
        reviews = extract_reviews(html)
        
        # Break the loop if no more reviews are found
        if not reviews:
            break

        all_reviews.extend(reviews)

    save_reviews_to_csv(all_reviews, output_file)

# Customize these parameters for the Apple App Store
url = 'https://apps.apple.com/us/app/google-photos-backup-edit/id962194608'  # Example URL, change as needed

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

scrape_app_store_reviews(url, headers=headers, max_pages=5000)
