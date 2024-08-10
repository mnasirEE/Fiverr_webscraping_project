import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open("a.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

# Find the relevant review data
spans = soup.find_all('span', {'class': 'a-size-base review-text review-text-content'})
span1 = soup.find_all('span', {'class': 'a-profile-name'})
titles = soup.find_all('a', {'data-hook': 'review-title'})
ratings = soup.find_all('span', {'class': 'a-icon-alt'})
dates = soup.find_all('span', {'data-hook': 'review-date'})

# Extract the text from the HTML elements and store in lists
reviews = [span.text.strip() for span in spans]
names = [span.text.strip() for span in span1]
titles_text = [title.find_all('span')[-1].text.strip() for title in titles]
ratings_text = [rating.text.strip()[0] for rating in ratings]
dates_text = [date.text.strip()[32:] for date in dates]

# Determine the maximum length of the lists
max_length = max(len(reviews), len(names), len(titles_text), len(ratings_text), len(dates_text))

# Ensure all lists are of the same length by padding with empty strings
reviews += [''] * (max_length - len(reviews))
names += [''] * (max_length - len(names))
titles_text += [''] * (max_length - len(titles_text))
ratings_text += [''] * (max_length - len(ratings_text))
dates_text += [''] * (max_length - len(dates_text))

# Create a DataFrame from the lists
df = pd.DataFrame({
    'Name': names,
    'Stars': ratings_text,
    'Date': dates_text,
    'Title': titles_text,
    'Amazon Photos Reviews': reviews
})

# Save the DataFrame to an Excel file
df.to_excel("amazon2.xlsx", index=False)

print(f"Scraped {len(reviews)} reviews")
