import pandas as pd
import os

# Set file paths
input_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\united_states_governors_1775_2020.csv"
output_dir = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files"
os.makedirs(output_dir, exist_ok=True)

# Create list of US states (excluding territories)
us_states = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
    'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
    'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
    'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
    'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
    'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
    'Wisconsin', 'Wyoming'
]

# Read and clean historical data
historical_df = pd.read_csv(input_file)
historical_df = historical_df[historical_df['state'].isin(us_states)]

# Create normalized data from historical records
normalized_data = []
years = range(2010, 2023)

for state in us_states:
    for year in years:
        state_year_data = historical_df[
            (historical_df['state'] == state) & 
            (historical_df['year'] == year)
        ]
        
        if not state_year_data.empty:
            governor = state_year_data.iloc[0]['governor']
            party = state_year_data.iloc[0]['party']
        else:
            governor = None
            party = None
            
        normalized_data.append({
            'year': year,
            'state': state,
            'governor': governor,
            'party': party
        })

# Create initial DataFrame
df = pd.DataFrame(normalized_data)

# Dictionary of updates for missing values
governor_updates = {
    'Alabama': {
        '2018-2022': {'governor': 'Kay Ivey', 'party': 'Republican'}
    },
    'Alaska': {
        '2019-2022': {'governor': 'Mike Dunleavy', 'party': 'Republican'}
    },
    'Arizona': {
        '2016-2022': {'governor': 'Doug Ducey', 'party': 'Republican'}
    },
    'Arkansas': {
        '2016-2022': {'governor': 'Asa Hutchinson', 'party': 'Republican'}
    },
    'California': {
        '2020-2022': {'governor': 'Gavin Newsom', 'party': 'Democrat'}
    },
    'Colorado': {
        '2020-2022': {'governor': 'Jared Polis', 'party': 'Democrat'}
    },
    'Connecticut': {
        '2020-2022': {'governor': 'Ned Lamont', 'party': 'Democrat'}
    },
    'Delaware': {
        '2018-2022': {'governor': 'John Carney', 'party': 'Democrat'}
    },
    'Florida': {
        '2020-2022': {'governor': 'Ron DeSantis', 'party': 'Republican'}
    },
    'Georgia': {
        '2020-2022': {'governor': 'Brian Kemp', 'party': 'Republican'}
    },
    'Hawaii': {
        '2015-2022': {'governor': 'David Ige', 'party': 'Democrat'}
    },
    'Idaho': {
        '2020-2022': {'governor': 'Brad Little', 'party': 'Republican'}
    },
    'Illinois': {
        '2020-2022': {'governor': 'J.B. Pritzker', 'party': 'Democrat'}
    },
    'Indiana': {
        '2018-2022': {'governor': 'Eric Holcomb', 'party': 'Republican'}
    },
    'Iowa': {
        '2018-2022': {'governor': 'Kim Reynolds', 'party': 'Republican'}
    },
    'Kansas': {
        '2020-2022': {'governor': 'Laura Kelly', 'party': 'Democrat'}
    },
    'Kentucky': {
        '2020-2022': {'governor': 'Andy Beshear', 'party': 'Democrat'}
    },
    'Louisiana': {
        '2017-2022': {'governor': 'John Bel Edwards', 'party': 'Democrat'}
    },
    'Maine': {
        '2020-2022': {'governor': 'Janet Mills', 'party': 'Democrat'}
    },
    'Maryland': {
        '2016-2022': {'governor': 'Larry Hogan', 'party': 'Republican'}
    },
    'Massachusetts': {
        '2016-2022': {'governor': 'Charlie Baker', 'party': 'Republican'}
    },
    'Michigan': {
        '2020-2022': {'governor': 'Gretchen Whitmer', 'party': 'Democrat'}
    },
    'Minnesota': {
        '2020-2022': {'governor': 'Tim Walz', 'party': 'Democrat'}
    },
    'Mississippi': {
        '2021-2022': {'governor': 'Tate Reeves', 'party': 'Republican'}
    },
    'Missouri': {
        '2019-2022': {'governor': 'Mike Parson', 'party': 'Republican'}
    },
    'Montana': {
        '2014-2020': {'governor': 'Steve Bullock', 'party': 'Democrat'},
        '2021-2022': {'governor': 'Greg Gianforte', 'party': 'Republican'}
    },
    'Nebraska': {
        '2016-2022': {'governor': 'Pete Ricketts', 'party': 'Republican'}
    },
    'Nevada': {
        '2020-2022': {'governor': 'Steve Sisolak', 'party': 'Democrat'}
    },
    'New Hampshire': {
        '2018-2022': {'governor': 'Chris Sununu', 'party': 'Republican'}
    },
    'New Jersey': {
        '2019-2022': {'governor': 'Phil Murphy', 'party': 'Democrat'}
    },
    'New Mexico': {
        '2020-2022': {'governor': 'Michelle Lujan Grisham', 'party': 'Democrat'}
    },
    'New York': {
        '2012-2021': {'governor': 'Andrew Cuomo', 'party': 'Democrat'},
        '2021-2022': {'governor': 'Kathy Hochul', 'party': 'Democrat'}
    },
    'North Carolina': {
        '2017-2022': {'governor': 'Roy Cooper', 'party': 'Democrat'}
    },
    'North Dakota': {
        '2017-2022': {'governor': 'Doug Burgum', 'party': 'Republican'}
    },
    'Ohio': {
        '2020-2022': {'governor': 'Mike DeWine', 'party': 'Republican'}
    },
    'Oklahoma': {
        '2020-2022': {'governor': 'Kevin Stitt', 'party': 'Republican'}
    },
    'Oregon': {
        '2016-2022': {'governor': 'Kate Brown', 'party': 'Democrat'}
    },
    'Pennsylvania': {
        '2016-2022': {'governor': 'Tom Wolf', 'party': 'Democrat'}
    },
    'Rhode Island': {
        '2016-2022': {'governor': 'Gina Raimondo', 'party': 'Democrat'}
    },
    'South Carolina': {
        '2018-2022': {'governor': 'Henry McMaster', 'party': 'Republican'}
    },
    'South Dakota': {
        '2020-2022': {'governor': 'Kristi Noem', 'party': 'Republican'}
    },
    'Tennessee': {
        '2020-2022': {'governor': 'Bill Lee', 'party': 'Republican'}
    },
    'Texas': {
        '2016-2022': {'governor': 'Greg Abbott', 'party': 'Republican'}
    },
    'Utah': {
        '2010-2020': {'governor': 'Gary Herbert', 'party': 'Republican'},
        '2021-2022': {'governor': 'Spencer Cox', 'party': 'Republican'}
    },
    'Vermont': {
        '2018-2022': {'governor': 'Phil Scott', 'party': 'Republican'}
    },
    'Virginia': {
        '2019-2021': {'governor': 'Ralph Northam', 'party': 'Democrat'},
        '2022': {'governor': 'Glenn Youngkin', 'party': 'Republican'}
    },
    'Washington': {
        '2014-2022': {'governor': 'Jay Inslee', 'party': 'Democrat'}
    },
    'West Virginia': {
        '2011-2014': {'governor': 'Earl Ray Tomblin', 'party': 'Democrat'},
        '2018-2022': {'governor': 'Jim Justice', 'party': 'Republican'}
    },
    'Wisconsin': {
        '2020-2022': {'governor': 'Tony Evers', 'party': 'Democrat'}
    },
    'Wyoming': {
        '2020-2022': {'governor': 'Mark Gordon', 'party': 'Republican'}
    }
}

# Function to update governor data
def update_governor_data(row):
    state = row['state']
    year = row['year']
    
    # Only update if current value is missing
    if pd.isna(row['governor']) or pd.isna(row['party']):
        if state in governor_updates:
            for period, info in governor_updates[state].items():
                if '-' in period:
                    start_year, end_year = map(int, period.split('-'))
                    if start_year <= year <= end_year:
                        return pd.Series({
                            'governor': info['governor'],
                            'party': info['party']
                        })
                elif int(period) == year:
                    return pd.Series({
                        'governor': info['governor'],
                        'party': info['party']
                    })
    
    return pd.Series({
        'governor': row['governor'],
        'party': row['party']
    })

# Apply updates only to missing values
df[['governor', 'party']] = df.apply(update_governor_data, axis=1)

# Sort the dataframe
df = df.sort_values(['state', 'year']).reset_index(drop=True)

# Save to CSV
output_file = os.path.join(output_dir, 'normalized_governors_2010_2022.csv')
df.to_csv(output_file, index=False)

# Print summary statistics
print(f"Data saved to {output_file}")
print("\nSummary:")
print(f"Total rows: {len(df)}")
print(f"Missing governor values: {df['governor'].isna().sum()}")
print(f"Missing party values: {df['party'].isna().sum()}")

# Print sample of updated data
print("\nSample of updated data:")
print(df.head(15))