import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import seaborn as sns

# File paths
homeless_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_rates.csv"
climate_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\climate_data\combined_climate_data_2010_2022.csv"
political_file = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\political_files\political_indices.csv"

# State abbreviation mapping
state_abbrev = {
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
    'WISCONSIN': 'WI', 'WYOMING': 'WY', 'DISTRICT OF COLUMBIA': 'DC'
}

def analyze_state_trends(homeless_df):
    """Analyze trends for each state"""
    state_trends = {}
    years = [str(year) for year in range(2010, 2023)]
    
    for _, row in homeless_df.iterrows():
        state = row['State']
        values = row[years].astype(float).values
        
        # Calculate trend using linear regression
        X = np.arange(len(values)).reshape(-1, 1)
        y = values.reshape(-1, 1)
        trend = np.polyfit(X.flatten(), y.flatten(), 1)[0]
        
        state_trends[state] = {
            'trend': trend,
            'mean': np.mean(values),
            'std': np.std(values),
            'min': np.min(values),
            'max': np.max(values)
        }
    
    return pd.DataFrame.from_dict(state_trends, orient='index')

def plot_state_trends(homeless_df, political_df, n_states=5):
    """Plot trends for top and bottom n states"""
    years = [str(year) for year in range(2010, 2023)]
    
    # Convert political state names to abbreviations
    political_df['State'] = political_df['State'].map(state_abbrev)
    
    # Calculate average political index for each state
    political_avg = political_df.groupby('State')['Political_Index'].mean()
    
    # Calculate overall changes
    changes = pd.DataFrame({
        'State': homeless_df['State'],
        'Change': homeless_df[years].astype(float).apply(lambda x: x.iloc[-1] - x.iloc[0], axis=1)
    })
    
    # Get top and bottom states
    top_states = changes.nlargest(n_states, 'Change')['State']
    bottom_states = changes.nsmallest(n_states, 'Change')['State']
    
    # Create plots
    plt.figure(figsize=(15, 10))
    
    # Plot top increasing states
    plt.subplot(2, 1, 1)
    for state in top_states:
        values = homeless_df[homeless_df['State'] == state][years].astype(float).iloc[0]
        color = 'blue' if political_avg[state] > 50 else 'red'
        plt.plot(years, values, marker='o', label=f"{state} ({political_avg[state]:.1f})", color=color)
    plt.title('States with Largest Increase in Homelessness\nBlue = Democratic, Red = Republican')
    plt.legend()
    plt.xticks(rotation=45)
    
    # Plot top decreasing states
    plt.subplot(2, 1, 2)
    for state in bottom_states:
        values = homeless_df[homeless_df['State'] == state][years].astype(float).iloc[0]
        color = 'blue' if political_avg[state] > 50 else 'red'
        plt.plot(years, values, marker='o', label=f"{state} ({political_avg[state]:.1f})", color=color)
    plt.title('States with Largest Decrease in Homelessness\nBlue = Democratic, Red = Republican')
    plt.legend()
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def main():
    # Read data
    homeless_df = pd.read_csv(homeless_file)
    political_df = pd.read_csv(political_file)
    
    # Analyze trends
    trend_analysis = analyze_state_trends(homeless_df)
    
    # Print analyses
    print("\nTop 5 States with Increasing Homelessness Trends:")
    print(trend_analysis.sort_values('trend', ascending=False).head())
    
    print("\nTop 5 States with Decreasing Homelessness Trends:")
    print(trend_analysis.sort_values('trend', ascending=True).head())
    
    print("\nOverall Statistics:")
    print(trend_analysis.describe())
    
    # Create visualizations
    plot_state_trends(homeless_df, political_df)

if __name__ == "__main__":
    main()
'''
This trend analysis shows the states with the largest increases in homelessness rates from 2010-2022. 
1. Vermont (VT)
Highest trend coefficient (11.77): Steepest increase in homelessness
Mean: Average of 234.39 homeless per 100,000 people
High variability (std: 81.01)
Range: From 172.65 to 429.60 per 100,000

2. New York (NY)
Second highest trend (7.44)
Highest mean rate (410.91)
More stable rates (std: 48.83)
Consistently high rates (325.37 to 473.39)

3. Delaware (DE)
Third steepest increase (5.46)
Lower mean rate (120.30)
High variability (std: 35.62)
Wide range: 94.58 to 232.38

4. California (CA)
Moderate increase (2.29)
High mean rate (325.03)
Very high variability (std: 66.74)
Extreme range: 146.81 to 439.34

5. South Dakota (SD)
Smallest increase among top 5 (2.13)
Lower mean rate (114.45)
More stable rates (std: 17.12)
Range: 89.57 to 152.66

Key Insights:
These states show the strongest upward trends in homelessness
Higher political index (more Democratic) states tend to show larger increases
States with higher mean rates also tend to have higher variability
The trends suggest growing challenges in these states despite different baseline rates
'''