import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# File paths
homeless_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_rates.csv"
climate_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\climate_data\combined_climate_data_2010_2022.csv"
political_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\political_files\political_indices.csv"

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

def prepare_data():
    # Read datasets
    homeless_df = pd.read_csv(homeless_file)
    climate_df = pd.read_csv(climate_file)
    political_df = pd.read_csv(political_file)
    
    # Convert homeless data to long format
    homeless_long = homeless_df.melt(id_vars=['State'], 
                                   var_name='Year', 
                                   value_name='Homeless_Rate')
    homeless_long['Year'] = homeless_long['Year'].astype(int)
    
    # Prepare climate data
    climate_clean = climate_df[['Name', 'Year', 'Value']].copy()
    climate_clean.columns = ['State', 'Year', 'Temperature']
    climate_clean['State'] = climate_clean['State'].map(state_mapping)
    
    # Prepare political data
    political_df['State'] = political_df['State'].str.title().map(state_mapping)
    
    # Merge datasets
    merged_df = pd.merge(homeless_long, climate_clean, on=['State', 'Year'])
    merged_df = pd.merge(merged_df, political_df, on=['State', 'Year'])
    
    return merged_df

def analyze_climate_political_relationship(df):
    # Create temperature categories
    df['Temp_Category'] = pd.qcut(df['Temperature'], 
                                 q=4, 
                                 labels=['Cold', 'Cool', 'Moderate', 'Warm'])
    
    # Create political categories
    df['Political_Category'] = pd.cut(df['Political_Index'],
                                    bins=[0, 33, 66, 100],
                                    labels=['Republican', 'Moderate', 'Democratic'])
    
    # Calculate statistics
    temp_stats = df.groupby('Temp_Category')['Homeless_Rate'].agg(['mean', 'std']).round(2)
    political_stats = df.groupby('Political_Category')['Homeless_Rate'].agg(['mean', 'std']).round(2)
    
    # Visualizations
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Temperature vs Homelessness
    sns.scatterplot(data=df, x='Temperature', y='Homeless_Rate', 
                   hue='Political_Category', ax=ax1)
    ax1.set_title('Temperature vs Homelessness Rate by Political Leaning')
    
    # 2. Political Index vs Homelessness
    sns.scatterplot(data=df, x='Political_Index', y='Homeless_Rate',
                   hue='Temp_Category', ax=ax2)
    ax2.set_title('Political Index vs Homelessness Rate by Temperature Zone')
    
    # 3. Box plots by temperature category
    sns.boxplot(data=df, x='Temp_Category', y='Homeless_Rate', ax=ax3)
    ax3.set_title('Homelessness Rate Distribution by Temperature Zone')
    
    # 4. Box plots by political category
    sns.boxplot(data=df, x='Political_Category', y='Homeless_Rate', ax=ax4)
    ax4.set_title('Homelessness Rate Distribution by Political Leaning')
    
    plt.tight_layout()
    plt.show()
    
    return temp_stats, political_stats

def main():
    # Prepare data
    merged_df = prepare_data()
    
    print("Data Overview:")
    print("\nShape:", merged_df.shape)
    print("\nFirst few rows:")
    print(merged_df.head())
    
    # Calculate correlations
    correlations = merged_df[['Homeless_Rate', 'Temperature', 'Political_Index']].corr()
    print("\nCorrelation Matrix:")
    print(correlations)
    
    # Analyze relationships
    temp_stats, political_stats = analyze_climate_political_relationship(merged_df)
    
    print("\nHomelessness Statistics by Temperature Category:")
    print(temp_stats)
    print("\nHomelessness Statistics by Political Category:")
    print(political_stats)
    
    # Run regression
    X = merged_df[['Temperature', 'Political_Index']]
    X = sm.add_constant(X)
    y = merged_df['Homeless_Rate']
    
    model = sm.OLS(y, X).fit()
    print("\nRegression Results:")
    print(model.summary())

if __name__ == "__main__":
    main()