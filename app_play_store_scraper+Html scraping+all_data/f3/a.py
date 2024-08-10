import pandas as pd
from app_store_scraper import AppStore

# Define all available country codes
all_countries = [
    'us', 'gb', 'ca', 'au', 'nz', 'sg', 'ie', 'al', 'dz', 'as', 'ad', 'ao',
    'ai', 'ag', 'ar', 'am', 'aw', 'at', 'az', 'bs', 'bh', 'bd', 'bb', 'by',
    'be', 'bz', 'bj', 'bm', 'bt', 'bo', 'ba', 'bw', 'br', 'vg', 'bn', 'bg',
    'bf', 'bi', 'kh', 'cm', 'cv', 'ky', 'cf', 'td', 'cl', 'cn', 'co', 'km',
    'cg', 'cd', 'cr', 'ci', 'hr', 'cy', 'cz', 'dk', 'dj', 'dm', 'do', 'ec',
    'eg', 'sv', 'gq', 'er', 'ee', 'et', 'fk', 'fo', 'fj', 'fi', 'fr', 'gf',
    'pf', 'ga', 'gm', 'ge', 'de', 'gh', 'gi', 'gr', 'gl', 'gd', 'gp', 'gu',
    'gt', 'gn', 'gw', 'gy', 'ht', 'hn', 'hk', 'hu', 'is', 'in', 'id', 'iq',
    'ie', 'il', 'it', 'jm', 'jp', 'jo', 'kz', 'ke', 'ki', 'kw', 'kg', 'la',
    'lv', 'lb', 'ls', 'lr', 'ly', 'li', 'lt', 'lu', 'mo', 'mk', 'mg', 'mw',
    'my', 'mv', 'ml', 'mt', 'mh', 'mq', 'mr', 'mu', 'yt', 'mx', 'fm', 'md',
    'mc', 'mn', 'me', 'ms', 'ma', 'mz', 'mm', 'na', 'nr', 'np', 'nl', 'nc',
    'nz', 'ni', 'ne', 'ng', 'nu', 'nf', 'kp', 'mp', 'no', 'om', 'pk', 'pw',
    'ps', 'pa', 'pg', 'py', 'pe', 'ph', 'pl', 'pt', 'pr', 'qa', 're', 'ro',
    'ru', 'rw', 'sh', 'kn', 'lc', 'pm', 'vc', 'ws', 'sm', 'st', 'sa', 'sn',
    'rs', 'sc', 'sl', 'sg', 'sk', 'si', 'sb', 'so', 'za', 'kr', 'es', 'lk',
    'sd', 'sr', 'sz', 'se', 'ch', 'sy', 'tw', 'tj', 'tz', 'th', 'tl', 'tg',
    'tk', 'to', 'tt', 'tn', 'tr', 'tm', 'tc', 'tv', 'vi', 'ug', 'ua', 'ae',
    'gb', 'us', 'uy', 'uz', 'vu', 'va', 've', 'vn', 'wf', 'eh', 'ye', 'zm',
    'zw'
]

# Initialize an empty list to store all reviews
all_reviews = []

for country in all_countries:
    # Initialize the AppStore object for each country
    gallery = AppStore(country=country, app_name='gallery-photo-vault', app_id='1450715436')
    
    # Fetch reviews in multiple requests until you get the desired number of reviews
    reviews = []
    total_fetched = 0
    while total_fetched < 2000:
        fetched_reviews = gallery.review(how_many=200)
        if not fetched_reviews:
            break
        total_fetched += len(fetched_reviews)
        reviews.extend(fetched_reviews)
    
    # Append reviews for the current country to the list of all reviews
    all_reviews.extend(reviews)

# Convert the reviews into a DataFrame
df = pd.DataFrame(all_reviews)

# Save DataFrame to CSV
df.to_csv('Slack-app-reviews.csv', index=False)
