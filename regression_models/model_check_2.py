import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# File paths
homeless_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_rates.csv"
climate_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\climate_data\combined_climate_data_2010_2022.csv"
political_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\political_files\political_indices.csv"
coc_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_raws\cocs_per_population.csv"

def prepare_data():
    # Read all datasets
    homeless_df = pd.read_csv(homeless_file)
    climate_df = pd.read_csv(climate_file)
    political_df = pd.read_csv(political_file)
    coc_df = pd.read_csv(coc_file)
    
    print("Initial data shapes:")
    print(f"Homeless data: {homeless_df.shape}")
    print(f"Climate data: {climate_df.shape}")
    print(f"Political data: {political_df.shape}")
    print(f"CoC data: {coc_df.shape}")
    
    # Print sample of each dataset
    print("\nSample of each dataset:")
    print("\nHomeless data first few rows:")
    print(homeless_df.head())
    print("\nClimate data first few rows:")
    print(climate_df.head())
    print("\nPolitical data first few rows:")
    print(political_df.head())
    print("\nCoC data first few rows:")
    print(coc_df.head())
    
    # Convert homeless data to long format
    homeless_long = homeless_df.melt(id_vars=['State'], 
                                   var_name='Year', 
                                   value_name='Homeless_Rate')
    homeless_long['Year'] = homeless_long['Year'].astype(int)
    
    # Prepare climate data
    climate_clean = climate_df[['Name', 'Year', 'Value']].copy()
    climate_clean.columns = ['State', 'Year', 'Temperature']
    
    # Standardize state names
    state_mapping = {
        'ALABAMA': 'AL', 'ALASKA': 'AK', 'ARIZONA': 'AZ', 'ARKANSAS': 'AR',
        'CALIFORNIA': 'CA', 'COLORADO': 'CO', 'CONNECTICUT': 'CT', 'DELAWARE': 'DE',
        'FLORIDA': 'FL', 'GEORGIA': 'GA', 'HAWAII': 'HI', 'IDAHO': 'ID',
        'ILLINOIS': 'IL', 'INDIANA': 'IN', 'IOWA': 'IA', 'KANSAS': 'KS',
        'KENTUCKY': 'KY', 'LOUISIANA': 'LA', 'MAINE': 'ME', 'MARYLAND': 'MD',
        'MASSACHUSETTS': 'MA', 'MICHIGAN': 'MI', 'MINNESOTA': 'MN', 'MISSISSIPPI': 'MS',
        'MISSOURI': 'MO', 'MONTANA': 'MT', 'NEBRASKA': 'NE', 'NEVADA': 'NV',
        'NEW HAMPSHIRE': 'NH', 'NEW JERSEY': 'NJ', 'NEW MEXICO': 'NM', 'NEW YORK': 'NY',
        'NORTH CAROLINA': 'NC', 'NORTH DAKOTA': 'ND', 'OHIO': 'OH', 'OKLAHOMA': 'OK',
        'OREGON': 'OR', 'PENNSYLVANIA': 'PA', 'RHODE ISLAND': 'RI', 'SOUTH CAROLINA': 'SC',
        'SOUTH DAKOTA': 'SD', 'TENNESSEE': 'TN', 'TEXAS': 'TX', 'UTAH': 'UT',
        'VERMONT': 'VT', 'VIRGINIA': 'VA', 'WASHINGTON': 'WA', 'WEST VIRGINIA': 'WV',
        'WISCONSIN': 'WI', 'WYOMING': 'WY', 'District of Columbia': 'DC'
    }
    
    # Apply state name standardization
    climate_clean['State'] = climate_clean['State'].str.upper().map(state_mapping)
    political_df['State'] = political_df['State'].map(state_mapping)
    
    # Merge datasets
    print("\nMerging datasets...")
    merged_df = pd.merge(homeless_long, climate_clean, on=['State', 'Year'])
    print(f"After homeless-climate merge: {merged_df.shape}")
    
    merged_df = pd.merge(merged_df, political_df, on=['State', 'Year'])
    print(f"After adding political data: {merged_df.shape}")
    
    merged_df = pd.merge(merged_df, coc_df[['State', 'Year', 'CoCs_per_hundredthousands']], on=['State', 'Year'])
    print(f"After adding CoC data: {merged_df.shape}")
    
    return merged_df

def analyze_correlations(df):
    corr = df[['Homeless_Rate', 'Temperature', 'Political_Index', 'CoCs_per_hundredthousands']].corr()
    
    # Create heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.show()
    
    return corr

def run_regression(df):
    # Prepare variables
    X = df[['Temperature', 'Political_Index', 'CoCs_per_hundredthousands']]
    X = sm.add_constant(X)
    y = df['Homeless_Rate']
    
    # Run regression
    model = sm.OLS(y, X).fit()
    return model

def main():
    # Prepare data
    merged_df = prepare_data()
    
    # Basic statistics
    print("\nBasic Statistics:")
    print(merged_df.describe())
    
    # Correlation analysis
    print("\nCorrelation Matrix:")
    corr = analyze_correlations(merged_df)
    print(corr)
    
    # Regression analysis
    if not merged_df.empty:
        model = run_regression(merged_df)
        print("\nRegression Results:")
        print(model.summary())
    
    # Save processed data
    output_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\processed_data.csv"
    merged_df.to_csv(output_file, index=False)
    print(f"\nProcessed data saved to: {output_file}")

if __name__ == "__main__":
    main()