import pandas as pd
import os

# Set the directory where your Excel files are located
directory = r'C:\Users\danny\OneDrive\Files\GitHub\research-lab-webscraping\Data'

# Initialize an empty list to store DataFrames
dataframes = []

for filename in os.listdir(directory):
    if filename.endswith('.xlsx') and not filename.startswith('~$'):
        file_path = os.path.join(directory, filename)
        df = pd.read_excel(file_path, header=1, skiprows=[0], skipfooter=3)  # Skip the first and second rows, last 3 rows
        
        # Check if '2000' is merged with an empty column 'H'
        if '2000' in df.columns and pd.isnull(df['2000'][0]):
            df['2000'] = df['2000'].combine_first(df['Unnamed: 7'])
            df.drop(columns=['Unnamed: 7'], inplace=True)
        
        dataframes.append(df)

# Concatenate the list of DataFrames into one DataFrame
combined_data = pd.concat(dataframes, ignore_index=True)

print(combined_data.head())
print(combined_data.tail())
print(combined_data.columns)

# Reshape the data
reshaped_data = pd.melt(
    combined_data,
    id_vars=['FIPS', 'Name', '2013 Rural-urban Continuum Code*'],
    var_name='Year',
    value_name='Percentage'
)

print(reshaped_data.columns)

# Split the 'Name' column into 'City' and 'State'
reshaped_data[['City', 'State']] = reshaped_data['Name'].str.split(', ', n=1, expand=True)

# Remove any extra whitespace in column headers and values
reshaped_data.columns = reshaped_data.columns.str.strip()
reshaped_data['Percentage'] = reshaped_data['Percentage'].astype(str).str.strip('%')

# Reorder columns as needed
reshaped_data = reshaped_data[['FIPS', 'City', 'State', '2013 Rural-urban Continuum Code*', 'Year', 'Percentage']]

# Save the reshaped data to a new Excel file
reshaped_data.to_excel(os.path.join(directory, 'reshaped_data.xlsx'), index=False)
