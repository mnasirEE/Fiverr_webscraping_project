import requests
import pandas as pd
from bs4 import BeautifulSoup

with open("google_play_2.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser") 

divs = soup.find_all('div', {'data-testid': 'review-content'})
names = soup.find_all('div', {'data-testid': 'reviewer-full-name'})
o = soup.find_all('span', {'class': 'text-neutral-80'})
r = soup.find_all('span', {'class': 'text-md text-neutral-80'})
date = soup.find_all('div', {'data-testid': 'review-written-on'})

reviews = []
Names = []
overall_rating = []
re = []
date1 =[]
for div in divs:
    reviews.append(div.text.strip())
for name in names:
    Names.append(name.text.strip())
for ov in o:
    overall_rating.append(ov.text.strip())
for rec in r:
    re.append(rec.text.strip())

for d in date:
    date1.append(d.text.strip())

# Make all arrays equal to the length of overall_rating
max_len = max(len(Names), len(reviews), len(overall_rating), len(re), len(date1))
Names += [''] * (max_len - len(Names))
reviews += [''] * (max_len - len(reviews))
overall_rating += [''] * (max_len - len(overall_rating))
re += [''] * (max_len - len(re))
date1 += [''] * (max_len - len(date1))

# Print lengths of arrays
print("Length of Names:", len(Names))
print("Length of Reviews:", len(reviews))
print("Length of Overall Rating:", len(overall_rating))
print("Length of Recommended Rating:", len(re))
print("Length of Date:", len(date1))

# Create a DataFrame
df = pd.DataFrame({'Name': Names,'iCloud Reviews': reviews, "rating": overall_rating, "recommended rating": re, "date": date1})
df.loc[90:, 'rating'] = pd.NA

# Save the modified DataFrame back to the CSV file
df.to_csv("icloud_actual.csv", index=False)
