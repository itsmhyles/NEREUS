import pandas as pd
import numpy as np

# File paths
file_2019 = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\nst-est2019-alldata.csv"
file_2023 = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\NST-EST2023-ALLDATA.csv"

try:
    # Read 2010-2019 data
    df_2019 = pd.read_csv(file_2019)
    
    # Read 2020-2022 data
    df_2023 = pd.read_csv(file_2023)
    
    # Filter rows for states only (SUMLEV = 40)
    df_2019 = df_2019[df_2019['SUMLEV'] == 40]
    df_2023 = df_2023[df_2023['SUMLEV'] == 40]
    
    # Create dictionary for column mapping (2010-2019)
    cols_2019 = {
        'NAME': 'State',
        'POPESTIMATE2010': '2010',
        'POPESTIMATE2011': '2011',
        'POPESTIMATE2012': '2012',
        'POPESTIMATE2013': '2013',
        'POPESTIMATE2014': '2014',
        'POPESTIMATE2015': '2015',
        'POPESTIMATE2016': '2016',
        'POPESTIMATE2017': '2017',
        'POPESTIMATE2018': '2018',
        'POPESTIMATE2019': '2019'
    }
    
    # Create dictionary for column mapping (2020-2022)
    cols_2023 = {
        'NAME': 'State',
        'POPESTIMATE2020': '2020',
        'POPESTIMATE2021': '2021',
        'POPESTIMATE2022': '2022'
    }
    
    # Select and rename columns for both datasets
    pop_2010_2019 = df_2019[cols_2019.keys()].rename(columns=cols_2019)
    pop_2020_2022 = df_2023[cols_2023.keys()].rename(columns=cols_2023)
    
    # Merge the datasets
    population_df = pd.merge(pop_2010_2019, pop_2020_2022, on='State', how='outer')
    
    # Create state abbreviation dictionary
    state_abbrev = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
        'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC',
        'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
        'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
        'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI',
        'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
        'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
        'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND',
        'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
        'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
        'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
        'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
        'Wisconsin': 'WI', 'Wyoming': 'WY'
    }
    
    # Convert state names to abbreviations
    population_df['State'] = population_df['State'].map(state_abbrev)
    
    # Reorder columns to ensure chronological order
    year_cols = [str(year) for year in range(2010, 2023)]
    final_cols = ['State'] + year_cols
    population_df = population_df[final_cols]
    
    # Save to CSV
    output_path = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\state_populations.csv"
    population_df.to_csv(output_path, index=False)
    
    print("Data successfully processed and saved!")
    print("\nFirst few rows of the combined data:")
    print(population_df.head())
    print("\nShape of the data:", population_df.shape)
    
    # Check for any missing values
    missing_values = population_df.isnull().sum()
    if missing_values.any():
        print("\nMissing values in the dataset:")
        print(missing_values[missing_values > 0])

except Exception as e:
    print(f"An error occurred: {str(e)}")