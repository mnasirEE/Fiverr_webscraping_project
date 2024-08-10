import pandas as pd
import random

# Attempt to read the CSV file with a different encoding
try:
    df = pd.read_csv("amazon_appstore_actual.csv", encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv("amazon_appstore_actual.csv", encoding='ISO-8859-1')

# Convert 'rating' column to numeric, coerce errors to NaN
df['Stars'] = pd.to_numeric(df['Stars'], errors='coerce')

# Replace NaN values (non-numeric and missing values) with random integer between 1 and 5
df['Stars'].fillna(random.randint(1, 5), inplace=True)

# Save the modified DataFrame back to the CSV file
df.to_csv("amazon_appstore_real.csv", index=False)

# Replace values in 'rating' column with NaN for rows beyond index 1002
df.loc[1000:, 'Date'] = pd.NA
df.loc[1000:, 'Stars'] = pd.NA

# Save the modified DataFrame back to the CSV file
df.to_csv("amazon_appstore_real.csv", index=False)



# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv("amazon_appstore_actual.csv", encoding='utf-8')

# # Replace values in 'rating' column with NaN for rows beyond index 1277
# df.loc[1002:, 'Date'] = pd.NA
# df.loc[1002:, 'Stars'] = pd.NA

# # Save the modified DataFrame back to the CSV file
# df.to_csv("amazon_appstore_real.csv", index=False)

