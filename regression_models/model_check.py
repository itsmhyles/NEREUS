import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
import statsmodels.api as sm

# File paths
homeless_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\homeless_data\homeless_rates.csv"
climate_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\climate_data\combined_climate_data_2010_2022.csv"
political_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\political_indices.csv"

# State mapping dictionary
state_mapping = {
    'AK': 'ALASKA', 'AL': 'ALABAMA', 'AR': 'ARKANSAS', 'AZ': 'ARIZONA',
    'CA': 'CALIFORNIA', 'CO': 'COLORADO', 'CT': 'CONNECTICUT', 'DE': 'DELAWARE',
    'FL': 'FLORIDA', 'GA': 'GEORGIA', 'HI': 'HAWAII', 'IA': 'IOWA',
    'ID': 'IDAHO', 'IL': 'ILLINOIS', 'IN': 'INDIANA', 'KS': 'KANSAS',
    'KY': 'KENTUCKY', 'LA': 'LOUISIANA', 'MA': 'MASSACHUSETTS', 'MD': 'MARYLAND',
    'ME': 'MAINE', 'MI': 'MICHIGAN', 'MN': 'MINNESOTA', 'MO': 'MISSOURI',
    'MS': 'MISSISSIPPI', 'MT': 'MONTANA', 'NC': 'NORTH CAROLINA', 'ND': 'NORTH DAKOTA',
    'NE': 'NEBRASKA', 'NH': 'NEW HAMPSHIRE', 'NJ': 'NEW JERSEY', 'NM': 'NEW MEXICO',
    'NV': 'NEVADA', 'NY': 'NEW YORK', 'OH': 'OHIO', 'OK': 'OKLAHOMA',
    'OR': 'OREGON', 'PA': 'PENNSYLVANIA', 'RI': 'RHODE ISLAND', 'SC': 'SOUTH CAROLINA',
    'SD': 'SOUTH DAKOTA', 'TN': 'TENNESSEE', 'TX': 'TEXAS', 'UT': 'UTAH',
    'VA': 'VIRGINIA', 'VT': 'VERMONT', 'WA': 'WASHINGTON', 'WI': 'WISCONSIN',
    'WV': 'WEST VIRGINIA', 'WY': 'WYOMING'
}

# Read data
homeless_df = pd.read_csv(homeless_file)
climate_df = pd.read_csv(climate_file)
political_df = pd.read_csv(political_file)

# Transform homeless data from wide to long format
homeless_long = pd.melt(
    homeless_df,
    id_vars=['State'],
    value_vars=[str(year) for year in range(2010, 2023)],
    var_name='Year',
    value_name='Homeless_Rate'
)
homeless_long['Year'] = pd.to_numeric(homeless_long['Year'])
homeless_long['State'] = homeless_long['State'].map(state_mapping)

# Prepare climate data
climate_clean = climate_df[['Name', 'Year', 'Value']].copy()
climate_clean.columns = ['State', 'Year', 'Temperature']
climate_clean['State'] = climate_clean['State'].str.upper()

# Verify data before merging
print("Homeless data shape:", homeless_long.shape)
print("Climate data shape:", climate_clean.shape)
print("Political data shape:", political_df.shape)

print("\nSample state names from each dataset:")
print("Homeless:", homeless_long['State'].unique()[:5])
print("Climate:", climate_clean['State'].unique()[:5])
print("Political:", political_df['State'].unique()[:5])

# Merge datasets
merged_df = pd.merge(homeless_long, political_df, on=['State', 'Year'], how='inner')
merged_df = pd.merge(merged_df, climate_clean, on=['State', 'Year'], how='inner')

# Remove any rows with missing values
merged_df = merged_df.dropna()

print("\nShape after merging:", merged_df.shape)
print("\nSample of merged data:")
print(merged_df.head())

if len(merged_df) > 0:
    # Add features
    merged_df['Homeless_Change'] = merged_df.groupby('State')['Homeless_Rate'].pct_change()
    merged_df['Temp_Volatility'] = merged_df.groupby('State')['Temperature'].transform(lambda x: x.std())
    merged_df['Political_Stability'] = merged_df.groupby('State')['Political_Index'].transform(lambda x: x.std())
    
    # Remove rows with NaN values after feature creation
    merged_df = merged_df.dropna()
    
    # Prepare features
    X = merged_df[['Political_Index', 'Temperature', 'Temp_Volatility', 'Political_Stability']]
    y = merged_df['Homeless_Rate']
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Compare models
    models = {
        'Linear': LinearRegression(),
        'Ridge': Ridge(),
        'Lasso': Lasso(),
        'Random Forest': RandomForestRegressor(random_state=42)
    }
    
    results = {}
    for name, model in models.items():
        scores = cross_val_score(model, X_scaled, y, cv=5)
        results[name] = {
            'Mean R2': scores.mean(),
            'Std R2': scores.std()
        }
    
    model_comparison = pd.DataFrame(results).T
    print("\nModel Comparison:")
    print(model_comparison)
    
    # Save results
    output_path = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\regression_results.csv"
    model_comparison.to_csv(output_path)
    
else:
    print("Error: No data available for modeling after preprocessing")


'''
Model Comparison:
                Mean R2    Std R2
Linear         0.222167  0.118116  # Poor fit
Ridge          0.222239  0.117883  # Similar to Linear
Lasso          0.222410  0.113922  # Similar to Linear
Random Forest  0.683626  0.109696  # Much better fit
'''