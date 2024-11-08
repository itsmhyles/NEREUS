import pandas as pd
import os

# Set file paths
input_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\1976-2020-president.csv"
output_dir = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files"
os.makedirs(output_dir, exist_ok=True)

# Read the data
df = pd.read_csv(input_file)

# Filter for years we're interested in (2008-2022)
election_years = [2008, 2012, 2016, 2020]  # Presidential election years
df = df[df['year'].isin(election_years)]

# Create empty list to store results
results = []

# Process each state
for state in df['state'].unique():
    last_result = None  # Store the last known election result
    
    # Process each year from 2010 to 2022
    for year in range(2008, 2023):
        if year in election_years:
            # Get election data for this year
            year_data = df[(df['year'] == year) & (df['state'] == state)]
            
            if len(year_data) > 0:
                # Calculate votes for Democrats and Republicans
                dem_votes = year_data[year_data['party_simplified'] == 'DEMOCRAT']['candidatevotes'].sum()
                rep_votes = year_data[year_data['party_simplified'] == 'REPUBLICAN']['candidatevotes'].sum()
                total_votes = dem_votes + rep_votes
                
                if total_votes > 0:
                    dem_percent = (dem_votes / total_votes) * 100
                    rep_percent = (rep_votes / total_votes) * 100
                    
                    # Determine winner and margin
                    if dem_percent > rep_percent:
                        winner = 'Democrat'
                        margin = ((dem_percent - rep_percent) / dem_percent) * 100
                    else:
                        winner = 'Republican'
                        margin = ((rep_percent - dem_percent) / rep_percent) * 100
                    
                    last_result = {
                        'dem_votes': dem_votes,
                        'rep_votes': rep_votes,
                        'dem_percent': dem_percent,
                        'rep_percent': rep_percent,
                        'winner': winner,
                        'margin': margin
                    }
        
        # Use last known result or carry forward previous result
        if last_result:
            results.append({
                'Year': year,
                'State': state,
                'Democrat_Votes': last_result['dem_votes'],
                'Republican_Votes': last_result['rep_votes'],
                'Democrat_Percentage': round(last_result['dem_percent'], 2),
                'Republican_Percentage': round(last_result['rep_percent'], 2),
                'Winner': last_result['winner'],
                'Margin': round(last_result['margin'], 2)
            })

# Create DataFrame
result_df = pd.DataFrame(results)

# Sort by State and Year
result_df = result_df.sort_values(['State', 'Year'])

# Save to CSV
output_file = os.path.join(output_dir, 'presidential_results_2010_2022_complete.csv')
result_df.to_csv(output_file, index=False)

# Print summary
print(f"Data saved to {output_file}")
print("\nSummary:")
print(f"Total rows: {len(result_df)}")
print("\nYears covered:")
print(result_df['Year'].unique())
print("\nSample of data:")
print(result_df.head(15))

# Verify completeness
year_state_counts = result_df.groupby('Year').size()
print("\nRows per year:")
print(year_state_counts)