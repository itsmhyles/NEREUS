import pandas as pd
import os

# Set file paths
input_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\1976-2020-senate.csv"
output_dir = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files"
os.makedirs(output_dir, exist_ok=True)

# Read the data
df = pd.read_csv(input_file)

# Filter for general elections
df = df[df['stage'] == 'gen']

# Create empty list to store results
results = []

# Dictionary to store last known results for each state
last_results = {}

# List of US states
us_states = [
    'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT',
    'DELAWARE', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA',
    'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN',
    'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE',
    'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO',
    'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
    'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA',
    'WISCONSIN', 'WYOMING'
]

# Process each year
for year in range(2010, 2023):
    year_data = df[df['year'] == year]
    
    # Process each state
    for state in us_states:
        state_data = year_data[year_data['state'] == state]
        
        if len(state_data) > 0:
            # Count winners by party for this election
            winners = []
            for special in [True, False]:
                special_data = state_data[state_data['special'] == special]
                if len(special_data) > 0:
                    winner = special_data.loc[special_data['candidatevotes'].idxmax()]
                    winners.append(winner['party_simplified'])
            
            # Update last known results for this state
            if winners:
                dem_count = winners.count('DEMOCRAT')
                rep_count = winners.count('REPUBLICAN')
                total_count = dem_count + rep_count
                
                if total_count > 0:
                    last_results[state] = {
                        'Democrat_Count': dem_count,
                        'Republican_Count': rep_count,
                        'Democrat_Percentage': (dem_count / total_count) * 100,
                        'Republican_Percentage': (rep_count / total_count) * 100
                    }
        
        # Add results for this year (either new or carried over)
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
output_file = os.path.join(output_dir, 'senate_representation_2010_2022_complete.csv')
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