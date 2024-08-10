# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv("google_photos.csv")

# # Convert 'rating' column to numeric, coerce errors to NaN
# df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# # Replace NaN values (non-numeric and missing values) with 3.0
# df['rating'].fillna(3.0, inplace=True)

# # Save the modified DataFrame back to the CSV file
# df.to_csv("google_photos_actual.csv", index=False)


import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("google_photos_actual.csv")

# Replace values in 'rating' column with NaN for rows beyond index 1277
df.loc[92:, 'rating'] = pd.NA

# Save the modified DataFrame back to the CSV file
df.to_csv("google_photos_capterra.csv", index=False)

