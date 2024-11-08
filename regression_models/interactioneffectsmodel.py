import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# File paths
homeless_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_rates.csv"
climate_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\climate_data\combined_climate_data_2010_2022.csv"
political_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\political_files\political_indices.csv"
coc_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_raws\cocs_per_population.csv"

def prepare_data():
    # Read datasets
    homeless_df = pd.read_csv(homeless_file)
    climate_df = pd.read_csv(climate_file)
    political_df = pd.read_csv(political_file)
    coc_df = pd.read_csv(coc_file)
    
    # Convert homeless data to long format
    homeless_long = pd.melt(homeless_df, 
                           id_vars=['State'], 
                           var_name='Year', 
                           value_name='Homeless_Rate')
    homeless_long['Year'] = homeless_long['Year'].astype(int)
    
    # Prepare climate data
    climate_clean = climate_df[['Name', 'Year', 'Value']].copy()
    climate_clean.columns = ['State', 'Year', 'Temperature']
    
    # State name mapping
    state_mapping = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
        'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
        'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
        'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
        'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
        'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
        'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
        'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
        'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
        'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
        'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
        'Wisconsin': 'WI', 'Wyoming': 'WY'
    }
    
    # Standardize state names
    climate_clean['State'] = climate_clean['State'].map(state_mapping)
    political_df['State'] = political_df['State'].str.title().map(state_mapping)
    
    # Merge datasets
    merged_df = pd.merge(homeless_long, climate_clean, on=['State', 'Year'])
    merged_df = pd.merge(merged_df, political_df, on=['State', 'Year'])
    merged_df = pd.merge(merged_df, coc_df[['State', 'Year', 'CoCs_per_hundredthousands']], 
                        on=['State', 'Year'])
    
    return merged_df

def analyze_interactions(df):
    """Analyze interaction effects between variables"""
    
    # Create interaction terms
    df['Temp_Political'] = df['Temperature'] * df['Political_Index']
    df['Temp_CoC'] = df['Temperature'] * df['CoCs_per_hundredthousands']
    df['Political_CoC'] = df['Political_Index'] * df['CoCs_per_hundredthousands']
    
    # Create categories for analysis
    df['Temp_Category'] = pd.qcut(df['Temperature'], q=3, 
                                 labels=['Cold', 'Moderate', 'Warm'])
    df['Political_Category'] = pd.qcut(df['Political_Index'], q=3, 
                                     labels=['Conservative', 'Moderate', 'Liberal'])
    df['CoC_Category'] = pd.qcut(df['CoCs_per_hundredthousands'], q=3, 
                                labels=['Low', 'Medium', 'High'])
    
    # Analyze each interaction type
    analyze_temp_political(df)
    analyze_temp_coc(df)
    analyze_political_coc(df)
    
    return df

def analyze_temp_political(df):
    plt.figure(figsize=(15, 5))
    
    # Scatter plot
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df, x='Temperature', y='Homeless_Rate', 
                   hue='Political_Category', size='Homeless_Rate',
                   sizes=(20, 200), alpha=0.6)
    plt.title('Temperature vs Homelessness by Political Leaning')
    
    # Interaction plot
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x='Temp_Category', y='Homeless_Rate', 
                hue='Political_Category')
    plt.title('Homelessness Rate by Temperature and Political Category')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def analyze_temp_coc(df):
    plt.figure(figsize=(15, 5))
    
    # Scatter plot
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df, x='Temperature', y='Homeless_Rate',
                   hue='CoC_Category', size='CoCs_per_hundredthousands',
                   sizes=(20, 200), alpha=0.6)
    plt.title('Temperature vs Homelessness by CoC Coverage')
    
    # Interaction plot
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x='Temp_Category', y='Homeless_Rate',
                hue='CoC_Category')
    plt.title('Homelessness Rate by Temperature and CoC Category')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def analyze_political_coc(df):
    plt.figure(figsize=(15, 5))
    
    # Scatter plot
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df, x='Political_Index', y='Homeless_Rate',
                   hue='CoC_Category', size='CoCs_per_hundredthousands',
                   sizes=(20, 200), alpha=0.6)
    plt.title('Political Index vs Homelessness by CoC Coverage')
    
    # Interaction plot
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x='Political_Category', y='Homeless_Rate',
                hue='CoC_Category')
    plt.title('Homelessness Rate by Political Leaning and CoC Category')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def main():
    # Prepare data
    print("Preparing data...")
    merged_df = prepare_data()
    
    # Analyze interactions
    print("\nAnalyzing interactions...")
    df_with_interactions = analyze_interactions(merged_df)
    
    # Calculate summary statistics
    print("\nSummary Statistics by Category:")
    print("\nBy Political Category:")
    print(df_with_interactions.groupby('Political_Category')['Homeless_Rate'].describe())
    
    print("\nBy Temperature Category:")
    print(df_with_interactions.groupby('Temp_Category')['Homeless_Rate'].describe())
    
    print("\nBy CoC Category:")
    print(df_with_interactions.groupby('CoC_Category')['Homeless_Rate'].describe())
    
    # Save results
    output_path = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\interaction_analysis_results.csv"
    df_with_interactions.to_csv(output_path, index=False)
    print(f"\nResults saved to: {output_path}")

if __name__ == "__main__":
    main()