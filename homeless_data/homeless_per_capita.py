import pandas as pd
import numpy as np

# Read the cleaned datasets
homeless_df = pd.read_csv(r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\homeless_counts.csv")
population_df = pd.read_csv(r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\state_populations.csv")

try:
    # Set State as index if it isn't already
    if 'State' in homeless_df.columns:
        homeless_df.set_index('State', inplace=True)
    if 'State' in population_df.columns:
        population_df.set_index('State', inplace=True)
    
    # Create empty DataFrame to store rates
    homeless_rate_df = pd.DataFrame(index=homeless_df.index)
    
    # Calculate homeless rate per 100,000 residents for each year
    for year in range(2010, 2023):  # Using 2010-2022 as these are the years we have for both datasets
        year_str = str(year)
        if year_str in homeless_df.columns and year_str in population_df.columns:
            homeless_rate_df[year_str] = (homeless_df[year_str] / population_df[year_str]) * 100000
    
    # Round to 2 decimal places
    homeless_rate_df = homeless_rate_df.round(2)
    
    # Save the rates to a new CSV file
    output_path = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\homeless_rates.csv"
    homeless_rate_df.to_csv(output_path)
    
    # Print some summary statistics
    print("Homelessness Rates per 100,000 residents")
    print("\nFirst few rows:")
    print(homeless_rate_df.head())
    
    print("\nSummary Statistics for 2022:")
    print(homeless_rate_df['2022'].describe())
    
    print("\nStates with highest homelessness rates in 2022:")
    print(homeless_rate_df['2022'].sort_values(ascending=False).head())
    
    print("\nStates with lowest homelessness rates in 2022:")
    print(homeless_rate_df['2022'].sort_values().head())
    
    # Check for any missing values
    missing_values = homeless_rate_df.isnull().sum()
    if missing_values.any():
        print("\nMissing values by year:")
        print(missing_values[missing_values > 0])

except Exception as e:
    print(f"An error occurred: {str(e)}")