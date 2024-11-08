import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

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
    
    print("\nCoC data columns:", coc_df.columns.tolist())
    
    # Define state mapping dictionary
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
    
    # Convert homeless data to long format
    homeless_long = pd.melt(homeless_df, 
                           id_vars=['State'], 
                           var_name='Year', 
                           value_name='Homeless_Rate')
    homeless_long['Year'] = homeless_long['Year'].astype(int)
    
    # Prepare climate data
    climate_clean = climate_df[['Name', 'Year', 'Value']].copy()
    climate_clean.columns = ['State', 'Year', 'Temperature']
    
    # Standardize state names
    climate_clean['State'] = climate_clean['State'].map(state_mapping)
    political_df['State'] = political_df['State'].str.title().map(state_mapping)
    
    # Print progress
    print("\nMerging datasets...")
    
    # First merge: Homeless and Climate
    merged_df = pd.merge(homeless_long, climate_clean, on=['State', 'Year'])
    print(f"After first merge: {merged_df.shape}")
    
    # Second merge: Add Political
    merged_df = pd.merge(merged_df, political_df, on=['State', 'Year'])
    print(f"After second merge: {merged_df.shape}")
    
    # Third merge: Add CoC
    merged_df = pd.merge(merged_df, coc_df[['State', 'Year', 'CoCs_per_hundredthousands']], 
                        on=['State', 'Year'])
    print(f"Final merge: {merged_df.shape}")
    
    # Print sample of final dataset
    print("\nSample of final merged dataset:")
    print(merged_df.head())
    
    return merged_df

def analyze_random_forest(merged_df):
    # Prepare features
    features = ['Temperature', 'Political_Index', 'CoCs_per_hundredthousands']
    X = merged_df[features]
    y = merged_df['Homeless_Rate']
    
    # Split and scale data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest
    rf_model = RandomForestRegressor(
        n_estimators=200,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42
    )
    
    rf_model.fit(X_train_scaled, y_train)
    y_pred = rf_model.predict(X_test_scaled)
    
    # Calculate metrics
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    # Feature importance
    importance = pd.DataFrame({
        'feature': features,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    # Visualizations
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Feature importance plot
    sns.barplot(data=importance, x='feature', y='importance', ax=ax1)
    ax1.set_title('Feature Importance')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    
    # Actual vs Predicted plot
    ax2.scatter(y_test, y_pred, alpha=0.5)
    ax2.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    ax2.set_xlabel('Actual Homeless Rate')
    ax2.set_ylabel('Predicted Homeless Rate')
    ax2.set_title('Actual vs Predicted Values')
    
    plt.tight_layout()
    plt.show()
    
    return {
        'model': rf_model,
        'r2': r2,
        'rmse': rmse,
        'feature_importance': importance,
        'scaler': scaler
    }

def main():
    # Prepare data
    print("Preparing data...")
    merged_df = prepare_data()
    
    if merged_df.empty:
        print("Error: No data after merging")
        return
    
    # Run Random Forest analysis
    print("\nRunning Random Forest analysis...")
    results = analyze_random_forest(merged_df)
    
    # Print results
    print("\nRandom Forest Results:")
    print(f"R² Score: {results['r2']:.4f}")
    print(f"RMSE: {results['rmse']:.4f}")
    print("\nFeature Importance:")
    print(results['feature_importance'])
    
    # Save results
    output_path = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\random_forest_results.csv"
    results['feature_importance'].to_csv(output_path, index=False)
    print(f"\nResults saved to: {output_path}")

if __name__ == "__main__":
    main()