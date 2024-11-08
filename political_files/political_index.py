import pandas as pd
import numpy as np

# File paths
senate_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\senate_representation_2010_2022_complete.csv"
house_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\house_representatives_2010_2022_complete.csv"
pres_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\presidential_results_2010_2022_complete.csv"
gov_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\normalized_governors_2010_2022.csv"

try:
    # Read the datasets
    senate_df = pd.read_csv(senate_file)
    house_df = pd.read_csv(house_file)
    pres_df = pd.read_csv(pres_file)
    gov_df = pd.read_csv(gov_file)
    
    # Standardize column names
    gov_df.columns = ['Year', 'State', 'Governor', 'Party']
    gov_df['Year'] = gov_df['Year'].astype(int)
    
    def calculate_political_index(year, state):
        try:
            # Senate Score (20%)
            senate_row = senate_df[(senate_df['Year'] == year) & (senate_df['State'] == state)]
            senate_score = senate_row['Democrat_Percentage'].iloc[0] * 0.20
            
            # House Score (20%)
            house_row = house_df[(house_df['Year'] == year) & (house_df['State'] == state)]
            house_score = house_row['Democrat_Percentage'].iloc[0] * 0.20
            
            # Governor Score (35%)
            gov_row = gov_df[(gov_df['Year'] == year) & (gov_df['State'].str.upper() == state)]
            gov_score = 100 if gov_row['Party'].iloc[0] == 'Democrat' else (50 if gov_row['Party'].iloc[0] == 'Independent' else 0)
            gov_score = gov_score * 0.35
            
            # Presidential Score (25%)
            pres_row = pres_df[(pres_df['Year'] == year) & (pres_df['State'] == state)]
            pres_score = pres_row['Democrat_Percentage'].iloc[0] * 0.25
            
            # Total Political Index (0-100 scale)
            return senate_score + house_score + gov_score + pres_score
            
        except Exception as e:
            print(f"Error calculating index for {state} in {year}: {str(e)}")
            return np.nan

    # Get unique states and years
    states = senate_df['State'].unique()
    years = range(2010, 2023)
    
    # Calculate index for all states and years
    political_indices = []
    for year in years:
        for state in states:
            index = calculate_political_index(year, state)
            political_indices.append({
                'Year': year,
                'State': state,
                'Political_Index': index
            })
    
    # Create DataFrame and save to CSV
    political_index_df = pd.DataFrame(political_indices)
    output_path = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_indices.csv"
    political_index_df.to_csv(output_path, index=False)
    
    # Print summary statistics
    print("\nPolitical Index Summary:")
    print(political_index_df.describe())
    print("\nSample of results:")
    print(political_index_df.head(10))
    
    # Check for missing values
    missing = political_index_df['Political_Index'].isna().sum()
    if missing > 0:
        print(f"\nWarning: {missing} missing values in the political index")

except Exception as e:
    print(f"Error in main execution: {str(e)}")