import requests
import pandas as pd
from bs4 import BeautifulSoup

# def fetch_data(path,url):
#     r= requests.get(url)
#     with open(path,"w") as f:
#         f.write(r.text)

# url = "https://www.azbar.org/for-lawyers/practice-tools-management/member-directory/"
# # fetch_data("arizon.html", url)
with open("b.html", "r", encoding="utf-8") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
div_h3YV2d = soup.find_all('div',{'class': "h3YV2d"})

reviews = []
for div in div_h3YV2d:
    reviews.append(div.text)
    
        
# Create a DataFrame
df = pd.DataFrame({'Amazon Photos Reviews': reviews})

# Save to Excel file
df.to_excel("output.xlsx", index=False)    
