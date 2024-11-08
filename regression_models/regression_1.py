import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# File paths
homeless_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\homeless_data\homeless_rates.csv"
climate_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\climate_data\combined_climate_data_2010_2022.csv"
political_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\political_indices.csv"

# Read the data
homeless_df = pd.read_csv(homeless_file)
climate_df = pd.read_csv(climate_file)
political_df = pd.read_csv(political_file)

# Create state name mapping dictionary
state_mapping = {
    'AK': 'ALASKA', 'AL': 'ALABAMA', 'AR': 'ARKANSAS', 'AZ': 'ARIZONA',
    'CA': 'CALIFORNIA', 'CO': 'COLORADO', 'CT': 'CONNECTICUT', 'DC': 'DISTRICT OF COLUMBIA',
    'DE': 'DELAWARE', 'FL': 'FLORIDA', 'GA': 'GEORGIA', 'HI': 'HAWAII',
    'IA': 'IOWA', 'ID': 'IDAHO', 'IL': 'ILLINOIS', 'IN': 'INDIANA',
    'KS': 'KANSAS', 'KY': 'KENTUCKY', 'LA': 'LOUISIANA', 'MA': 'MASSACHUSETTS',
    'MD': 'MARYLAND', 'ME': 'MAINE', 'MI': 'MICHIGAN', 'MN': 'MINNESOTA',
    'MO': 'MISSOURI', 'MS': 'MISSISSIPPI', 'MT': 'MONTANA', 'NC': 'NORTH CAROLINA',
    'ND': 'NORTH DAKOTA', 'NE': 'NEBRASKA', 'NH': 'NEW HAMPSHIRE', 'NJ': 'NEW JERSEY',
    'NM': 'NEW MEXICO', 'NV': 'NEVADA', 'NY': 'NEW YORK', 'OH': 'OHIO',
    'OK': 'OKLAHOMA', 'OR': 'OREGON', 'PA': 'PENNSYLVANIA', 'RI': 'RHODE ISLAND',
    'SC': 'SOUTH CAROLINA', 'SD': 'SOUTH DAKOTA', 'TN': 'TENNESSEE', 'TX': 'TEXAS',
    'UT': 'UTAH', 'VA': 'VIRGINIA', 'VT': 'VERMONT', 'WA': 'WASHINGTON',
    'WI': 'WISCONSIN', 'WV': 'WEST VIRGINIA', 'WY': 'WYOMING'
}

# Convert homeless_rates from wide to long format
homeless_long = homeless_df.melt(id_vars=['State'], 
                                var_name='Year', 
                                value_name='Homeless_Rate')
homeless_long['Year'] = homeless_long['Year'].astype(int)
homeless_long['State'] = homeless_long['State'].map(state_mapping)

# Prepare climate data (select only needed columns and rename)
climate_panel = climate_df[['Name', 'Year', 'Value']].copy()
climate_panel.columns = ['State', 'Year', 'Temperature']
climate_panel['State'] = climate_panel['State'].str.upper()

# Political data is already in the correct format, just ensure state names are uppercase
political_df['State'] = political_df['State'].str.upper()

# First merge homeless and political data
print("Shapes before merging:")
print(f"Homeless data: {homeless_long.shape}")
print(f"Political data: {political_df.shape}")
print(f"Climate data: {climate_panel.shape}")

# Perform merges
merged_df = pd.merge(homeless_long, political_df, 
                    on=['State', 'Year'], 
                    how='inner')
merged_df = pd.merge(merged_df, climate_panel, 
                    on=['State', 'Year'], 
                    how='inner')

print("\nShape after merges:", merged_df.shape)
print("\nSample of final merged data:")
print(merged_df.head())

# Check for missing values
print("\nMissing values:")
print(merged_df.isnull().sum())

# Calculate correlations
correlations = merged_df[['Homeless_Rate', 'Political_Index', 'Temperature']].corr()
print("\nCorrelation Matrix:")
print(correlations)

# Create visualizations
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Political Index vs Homelessness
sns.scatterplot(data=merged_df, x='Political_Index', y='Homeless_Rate', ax=ax1)
ax1.set_title('Political Index vs Homelessness Rate')
ax1.set_xlabel('Political Index (Higher = More Democratic)')
ax1.set_ylabel('Homelessness Rate per 100,000')

# Plot 2: Temperature vs Homelessness
sns.scatterplot(data=merged_df, x='Temperature', y='Homeless_Rate', ax=ax2)
ax2.set_title('Temperature vs Homelessness Rate')
ax2.set_xlabel('Temperature (°F)')
ax2.set_ylabel('Homelessness Rate per 100,000')

plt.tight_layout()
plt.show()

# Run regression
X = merged_df[['Political_Index', 'Temperature']]
y = merged_df['Homeless_Rate']
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print("\nRegression Results:")
print(model.summary())

# Save merged data
output_path = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\merged_data.csv"
merged_df.to_csv(output_path, index=False)