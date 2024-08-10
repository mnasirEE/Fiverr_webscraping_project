import pandas as pd
import glob

# List all CSV files in the current directory
files = glob.glob("*.csv")

# Initialize an empty list to store DataFrames
dfs = []

# Loop through each CSV file and read its data
for file in files:
    try:
        # Read the CSV file, specifying encoding
        df = pd.read_csv(file, encoding='utf-8-sig')
        # Append the DataFrame to the list
        dfs.append(df)
    except UnicodeDecodeError:
        print(f"Error reading file: {file}. Skipping...")

# Concatenate all DataFrames in the list into a single DataFrame
combined_data = pd.concat(dfs, ignore_index=True)

# Save the combined data to a new CSV file
combined_data.to_csv("combined_data.csv", index=False)
