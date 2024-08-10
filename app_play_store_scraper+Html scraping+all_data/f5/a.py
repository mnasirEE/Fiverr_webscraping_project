import os
import pandas as pd

# Get the current working directory
current_directory = os.getcwd()

# Path to the directory containing CSV files
csv_directory = os.path.join(current_directory, 'd')

# List all files in the CSV directory
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

# Initialize an empty list to store DataFrames
dfs = []

# Loop through each CSV file, read it, and append its DataFrame to dfs list
for file in csv_files:
    file_path = os.path.join(csv_directory, file)
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        dfs.append(df)
    except UnicodeDecodeError:
        print(f"UnicodeDecodeError: Unable to decode file '{file}'")

# Concatenate all DataFrames into a single DataFrame
combined_data = pd.concat(dfs, ignore_index=True)

# Now you can use the combined_data DataFrame for further analysis or processing
# Save the combined data to a new CSV file
combined_data.to_csv("combined_data.csv", index=False)
