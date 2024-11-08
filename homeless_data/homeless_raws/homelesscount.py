import pandas as pd
import numpy as np
import os

# Set the file path
file_path = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\2007-2023-PIT-Counts-by-State.xlsb"

# Initialize an empty dictionary to store data from all years
homeless_data = {}

# Years to process
years = range(2010, 2023)  # Changed to 2022 as discussed earlier and changed to 2010 as per census limitation

try:
    # Read each sheet (year) from the file
    for year in years:
        try:
            # Read the specific sheet
            df = pd.read_excel(file_path, sheet_name=str(year), engine='pyxlsb')
            
            # Select the correct columns (adjust these based on actual column names)
            state_col = df.columns[0]  # First column should be State
            total_col = df.columns[2]  # Third column should be Total
            
            df = df[[state_col, total_col]]
            
            # Convert empty strings, zeros, and other potential null values to NaN
            df[total_col] = pd.to_numeric(df[total_col], errors='coerce')
            
            # Remove any rows where State is null
            df = df.dropna(subset=[state_col])
            
            # Remove the total row (case-insensitive match)
            df = df[~df[state_col].str.lower().str.contains('total', na=False)]
            
            # Store in dictionary with year as key
            homeless_data[year] = df.set_index(state_col)[total_col]
            
            print(f"Successfully processed year {year}")
            print(f"Number of states with data: {df[~df[total_col].isna()].shape[0]}")
            print(f"Number of states with missing data: {df[df[total_col].isna()].shape[0]}")
            
        except Exception as e:
            print(f"Error processing year {year}: {str(e)}")
            continue

    # Create a combined DataFrame
    combined_df = pd.DataFrame(homeless_data)
    
    # Print data quality report
    print("\nData Quality Report:")
    print(f"Total number of states/territories: {len(combined_df)}")
    print("\nMissing data by year:")
    print(combined_df.isna().sum())
    
    print("\nMissing data by state:")
    print(combined_df.isna().sum(axis=1)[combined_df.isna().sum(axis=1) > 0])
    
    # Save to CSV for easier handling later
    output_path = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\homeless_counts.csv"
    combined_df.to_csv(output_path)
    
    print("\nData successfully processed and saved!")
    print(f"Shape of combined data: {combined_df.shape}")
    print("\nFirst few rows of the combined data:")
    print(combined_df.head())

except Exception as e:
    print(f"An error occurred: {str(e)}")