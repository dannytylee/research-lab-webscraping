# unncessary

import os
import pandas as pd

# Set the directory where your Excel files are located
directory = r'C:\Users\danny\OneDrive\Files\GitHub\research-lab-webscraping\Result'

# Iterate through all Excel files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(directory, filename)
        
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        
        # Remove rows where 'State' column is empty
        df = df.dropna(subset=['State'])
        
        # Format 'FIPS' column to have 5 digits
        df['FIPS'] = df['FIPS'].apply(lambda x: str(x).zfill(5))
        
        # Change column name from 'City' to 'County'
        df.rename(columns={'City': 'County'}, inplace=True)
        
        # Save the modified DataFrame back to the Excel file
        df.to_excel(file_path, index=False)
        
        print(f"Processed: {filename}")

print("All files processed.")
