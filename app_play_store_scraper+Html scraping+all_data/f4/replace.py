# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv("icloud_replaced.csv")

# # Convert 'rating' column to numeric, coerce errors to NaN
# df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# # Replace NaN values (non-numeric and missing values) with 3.0
# df['rating'].fillna(3.0, inplace=True)

# # Save the modified DataFrame back to the CSV file
# df.to_csv("icloud_review_3.csv", index=False)

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("icloud_review_3.csv")

# Replace values in 'rating' column with NaN for rows beyond index 1277
df.loc[1277:, 'rating'] = pd.NA

# Save the modified DataFrame back to the CSV file
df.to_csv("icloud_actual.csv", index=False)

