import pandas as pd
import numpy as np

# File paths
coc_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_per_state\2007-2023-PIT-Counts-by-State.xlsb"
pop_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_raws\state_populations.csv"
output_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_raws\cocs_per_population.csv"

def get_coc_counts(year):
    """Extract CoC counts for a specific year"""
    df = pd.read_excel(coc_file, sheet_name=str(year), engine='pyxlsb')
    # Get CoC counts (second column)
    coc_counts = df[['State', 'Number of CoCs']].copy()
    coc_counts['Year'] = year
    return coc_counts

def process_coc_data():
    """Combine CoC counts from 2010-2022"""
    all_coc_counts = []
    
    for year in range(2010, 2023):
        try:
            year_counts = get_coc_counts(year)
            all_coc_counts.append(year_counts)
        except Exception as e:
            print(f"Error processing year {year}: {str(e)}")
    
    # Combine all years
    coc_df = pd.concat(all_coc_counts, ignore_index=True)
    return coc_df

def calculate_cocs_per_population():
    """Calculate CoCs per million population"""
    # Read population data
    pop_df = pd.read_csv(pop_file)
    
    # Get CoC counts
    coc_df = process_coc_data()
    
    # Initialize results
    results = []
    
    # Calculate rates for each state and year
    for year in range(2010, 2023):
        year_cocs = coc_df[coc_df['Year'] == year]
        
        for _, row in year_cocs.iterrows():
            state = row['State']
            cocs = row['Number of CoCs']
            
            try:
                # Get population for this state and year
                population = pop_df.loc[pop_df['State'] == state, str(year)].iloc[0]
                
                # Calculate CoCs per million
                cocs_per_million = (cocs * 1000000) / population
                
                results.append({
                    'State': state,
                    'Year': year,
                    'CoCs': cocs,
                    'Population': population,
                    'CoCs_per_million': cocs_per_million
                })
            except Exception as e:
                print(f"Error calculating rate for {state} in {year}: {str(e)}")
    
    return pd.DataFrame(results)

def main():
    # Calculate CoCs per population
    results_df = calculate_cocs_per_population()
    
    # Save detailed results
    results_df.to_csv(output_file, index=False)
    
    # Print summary statistics
    print("\nCoCs per Million Population Summary:")
    print(results_df.groupby('Year')['CoCs_per_million'].describe())
    
    print("\nStates with Highest Average CoCs per Million:")
    state_avg = results_df.groupby('State')['CoCs_per_million'].mean().sort_values(ascending=False)
    print(state_avg.head())
    
    print("\nStates with Lowest Average CoCs per Million:")
    print(state_avg.tail())
    
    # Create wide format for time series analysis
    wide_df = results_df.pivot(index='State', 
                              columns='Year', 
                              values='CoCs_per_million')
    wide_df.to_csv(output_file.replace('.csv', '_wide.csv'))

if __name__ == "__main__":
    main()