import pandas as pd
import numpy as np
import os

# Set file paths
input_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\1976-2022-house.csv"
output_dir = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files"
os.makedirs(output_dir, exist_ok=True)

# Define state representative counts (as of 2020)
state_representatives = {
    'ALABAMA': 7,
    'ALASKA': 1,
    'ARIZONA': 9,
    'ARKANSAS': 4,
    'CALIFORNIA': 53,
    'COLORADO': 7,
    'CONNECTICUT': 5,
    'DELAWARE': 1,
    'FLORIDA': 27,
    'GEORGIA': 14,
    'HAWAII': 2,
    'IDAHO': 2,
    'ILLINOIS': 18,
    'INDIANA': 9,
    'IOWA': 4,
    'KANSAS': 4,
    'KENTUCKY': 6,
    'LOUISIANA': 6,
    'MAINE': 2,
    'MARYLAND': 8,
    'MASSACHUSETTS': 9,
    'MICHIGAN': 14,
    'MINNESOTA': 8,
    'MISSISSIPPI': 4,
    'MISSOURI': 8,
    'MONTANA': 1,
    'NEBRASKA': 3,
    'NEVADA': 4,
    'NEW HAMPSHIRE': 2,
    'NEW JERSEY': 12,
    'NEW MEXICO': 3,
    'NEW YORK': 27,
    'NORTH CAROLINA': 13,
    'NORTH DAKOTA': 1,
    'OHIO': 16,
    'OKLAHOMA': 5,
    'OREGON': 5,
    'PENNSYLVANIA': 18,
    'RHODE ISLAND': 2,
    'SOUTH CAROLINA': 7,
    'SOUTH DAKOTA': 1,
    'TENNESSEE': 9,
    'TEXAS': 36,
    'UTAH': 4,
    'VERMONT': 1,
    'VIRGINIA': 11,
    'WASHINGTON': 10,
    'WEST VIRGINIA': 3,
    'WISCONSIN': 8,
    'WYOMING': 1
}

# Read the data
df = pd.read_csv(input_file)

# Filter for general elections
df = df[df['stage'] == 'GEN']

# Define election years (House elections every 2 years)
election_years = [2010, 2012, 2014, 2016, 2018, 2020, 2022]

results = []
last_results = {}  # Store the last known results for each state

for year in range(2010, 2023):
    # If it's an election year, calculate new results
    if year in election_years:
        year_data = df[df['year'] == year]
        
        for state, num_representatives in state_representatives.items():
            state_data = year_data[year_data['state'] == state]
            
            if len(state_data) > 0:
                winners = []
                for district in state_data['district'].unique():
                    district_data = state_data[state_data['district'] == district]
                    if len(district_data) > 0:
                        winner = district_data.loc[district_data['candidatevotes'].idxmax()]
                        winners.append(winner['party'])
                
                dem_count = winners.count('DEMOCRAT')
                rep_count = winners.count('REPUBLICAN')
                total_count = dem_count + rep_count
                
                if total_count > 0:
                    dem_percent = (dem_count / total_count) * 100
                    rep_percent = (rep_count / total_count) * 100
                else:
                    dem_percent = 0
                    rep_percent = 0
                
                # Store the results for this state
                last_results[state] = {
                    'Democrat_Count': dem_count,
                    'Republican_Count': rep_count,
                    'Democrat_Percentage': dem_percent,
                    'Republican_Percentage': rep_percent
                }
    
    # Add results for this year (either new results or carried over)
    for state in state_representatives.keys():
        if state in last_results:
            results.append({
                'Year': year,
                'State': state,
                'Democrat_Count': last_results[state]['Democrat_Count'],
                'Republican_Count': last_results[state]['Republican_Count'],
                'Democrat_Percentage': last_results[state]['Democrat_Percentage'],
                'Republican_Percentage': last_results[state]['Republican_Percentage']
            })
        else:
            # If we don't have any results yet, add empty row
            results.append({
                'Year': year,
                'State': state,
                'Democrat_Count': 0,
                'Republican_Count': 0,
                'Democrat_Percentage': 0,
                'Republican_Percentage': 0
            })

# Create DataFrame
result_df = pd.DataFrame(results)

# Sort by State and Year
result_df = result_df.sort_values(['State', 'Year'])

# Save to CSV
output_file = os.path.join(output_dir, 'house_representatives_2010_2022_complete.csv')
result_df.to_csv(output_file, index=False)

# Print summary
print(f"Data saved to {output_file}")
print("\nSummary:")
print(f"Total rows: {len(result_df)}")
print("\nYearly totals:")
print(result_df.groupby('Year')[['Democrat_Count', 'Republican_Count']].sum())

# Verify completeness
year_state_counts = result_df.groupby('Year').size()
print("\nRows per year:")
print(year_state_counts)