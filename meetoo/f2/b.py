# Import packages
import time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium setup
options = Options()
options.headless = True  # Runs Chrome in headless mode.
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

# Update the path to the location of your ChromeDriver
service = Service(r'C:\Users\vc\Downloads\chrome-win64\chrome-win64')
driver = webdriver.Chrome(service=service, options=options)

# URL of the Amazon Review page
reviews_url = 'https://www.amazon.com/Amazon-com-Amazon-Photos/dp/B00A11AN6O'

# Define Page No
len_page = 70

# Function to get reviews HTML with Selenium
def reviewsHtml(url, len_page):
    soups = []
    
    for page_no in range(1, len_page + 1):
        driver.get(f'{url}/ref=cm_cr_getr_d_paging_btm_next_{page_no}?pageNumber={page_no}&reviewerType=all_reviews&filterByStar=critical')

        # Wait for the reviews to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-hook="review"]'))
        )
        
        # Click on "Show more" buttons
        while True:
            try:
                show_more_button = driver.find_element(By.CSS_SELECTOR, 'span[data-action="reviews:filter-action"]')
                driver.execute_script("arguments[0].click();", show_more_button)
                # Wait for new content to load
                time.sleep(2)
            except:
                break

        # Get the page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'lxml')
        soups.append(soup)
    
    return soups

# Grab reviews name, description, date, stars, title from HTML
def getReviews(html_data):
    data_dicts = []

    boxes = html_data.select('div[data-hook="review"]')
    
    for box in boxes:
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
            datetime_str = box.select_one('[data-hook="review-date"]').text.strip().split(' on ')[-1]
            date = datetime.strptime(datetime_str, '%B %d, %Y').strftime("%d/%m/%Y")
        except Exception as e:
            date = 'N/A'

        try:
            description = box.select_one('[data-hook="review-body"]').text.strip()
        except Exception as e:
            description = 'N/A'

        data_dict = {
            'Name': name,
            'Stars': stars,
            'Title': title,
            'Date': date,
            'Description': description
        }

        data_dicts.append(data_dict)
    
    return data_dicts

# Grab all HTML
html_datas = reviewsHtml(reviews_url, len_page)

# Empty List to Hold all reviews data
reviews = []

for html_data in html_datas:
    review = getReviews(html_data)
    reviews += review

# Create a dataframe with reviews data
df_reviews = pd.DataFrame(reviews)

# Save data
df_reviews.to_csv('amazon_reviews_on_Amazon.csv', index=False)

# Close the Selenium browser session
driver.quit()
