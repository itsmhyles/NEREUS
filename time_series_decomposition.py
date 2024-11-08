import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# File paths
homeless_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\homeless_data\homeless_rates.csv"
climate_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\climate_data\combined_climate_data_2010_2022.csv"
political_file = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\political_files\political_indices.csv"

def load_and_prepare_data():
    # Read data
    homeless_df = pd.read_csv(homeless_file)
    climate_df = pd.read_csv(climate_file)
    political_df = pd.read_csv(political_file)
    
    # Convert homeless data to long format
    homeless_long = homeless_df.melt(
        id_vars=['State'], 
        var_name='Year', 
        value_name='Homeless_Rate'
    )
    homeless_long['Year'] = homeless_long['Year'].astype(int)
    
    # Prepare climate data
    climate_panel = climate_df[['Name', 'Year', 'Value']].copy()
    climate_panel.columns = ['State', 'Year', 'Temperature']
    
    # Standardize state names
    homeless_long['State'] = homeless_long['State'].str.upper()
    climate_panel['State'] = climate_panel['State'].str.upper()
    
    # Merge datasets
    merged_df = pd.merge(homeless_long, political_df, on=['State', 'Year'])
    merged_df = pd.merge(merged_df, climate_panel, on=['State', 'Year'])
    
    return merged_df

def analyze_time_series(df):
    """Perform comprehensive time series analysis"""
    
    # 1. Overall Trends
    yearly_stats = df.groupby('Year').agg({
        'Homeless_Rate': ['mean', 'std', 'min', 'max'],
        'Political_Index': 'mean',
        'Temperature': 'mean'
    })
    
    # 2. State-specific trends
    state_trends = {}
    for state in df['State'].unique():
        state_data = df[df['State'] == state].sort_values('Year')
        
        # Perform decomposition
        try:
            decomposition = seasonal_decompose(
                state_data['Homeless_Rate'], 
                period=4,  # Adjust period based on your data
                model='additive'
            )
            
            state_trends[state] = {
                'trend': decomposition.trend,
                'seasonal': decomposition.seasonal,
                'resid': decomposition.resid,
                'mean_rate': state_data['Homeless_Rate'].mean(),
                'trend_direction': np.polyfit(range(len(state_data)), 
                                           state_data['Homeless_Rate'], 1)[0]
            }
        except:
            print(f"Could not decompose series for {state}")
    
    return yearly_stats, state_trends

def create_visualizations(df, yearly_stats, state_trends):
    # 1. Overall Trends Plot
    plt.figure(figsize=(15, 10))
    
    # Plot 1: National Trends
    plt.subplot(2, 2, 1)
    plt.plot(yearly_stats.index, yearly_stats[('Homeless_Rate', 'mean')], 'b-')
    plt.fill_between(yearly_stats.index, 
                     yearly_stats[('Homeless_Rate', 'min')],
                     yearly_stats[('Homeless_Rate', 'max')],
                     alpha=0.2)
    plt.title('National Homelessness Trends')
    plt.xlabel('Year')
    plt.ylabel('Homeless Rate')
    
    # Plot 2: State Variations
    plt.subplot(2, 2, 2)
    trend_directions = pd.Series({state: data['trend_direction'] 
                                for state, data in state_trends.items()})
    trend_directions.sort_values().plot(kind='bar')
    plt.title('State-wise Trend Directions')
    plt.xticks(rotation=90)
    
    # Plot 3: Political vs Homelessness
    plt.subplot(2, 2, 3)
    sns.scatterplot(data=df, x='Political_Index', y='Homeless_Rate', 
                   hue='Year', alpha=0.6)
    plt.title('Political Index vs Homelessness')
    
    # Plot 4: Temperature vs Homelessness
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=df, x='Temperature', y='Homeless_Rate', 
                   hue='Year', alpha=0.6)
    plt.title('Temperature vs Homelessness')
    
    plt.tight_layout()
    plt.show()

def analyze_state_clusters(df):
    """Cluster states based on their homelessness patterns"""
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    
    # Prepare features for clustering
    features = ['Homeless_Rate', 'Political_Index', 'Temperature']
    X = df[features]
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Perform clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)
    
    return df

def main():
    # Load and prepare data
    df = load_and_prepare_data()
    
    # Perform time series analysis
    yearly_stats, state_trends = analyze_time_series(df)
    
    # Create visualizations
    create_visualizations(df, yearly_stats, state_trends)
    
    # Perform clustering analysis
    df_clustered = analyze_state_clusters(df)
    
    # Print summary statistics
    print("\nYearly Statistics:")
    print(yearly_stats)
    
    print("\nTop 5 States with Increasing Trends:")
    trend_directions = pd.Series({state: data['trend_direction'] 
                                for state, data in state_trends.items()})
    print(trend_directions.nlargest(5))
    
    print("\nTop 5 States with Decreasing Trends:")
    print(trend_directions.nsmallest(5))
    
    # Save results
    output_path = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\time_series_analysis_results.csv"
    yearly_stats.to_csv(output_path)

if __name__ == "__main__":
    main()