import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns

def prepare_data():
    # Read datasets
    homeless_df = pd.read_csv(r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_rates.csv")
    climate_df = pd.read_csv(r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\climate_data\combined_climate_data_2010_2022.csv")
    political_df = pd.read_csv(r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\political_files\political_indices.csv")
    coc_df = pd.read_csv(r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\homeless_data\homeless_raws\cocs_per_population.csv")
    
    print("\nInitial shapes:")
    print(f"Homeless data: {homeless_df.shape}")
    print(f"Climate data: {climate_df.shape}")
    print(f"Political data: {political_df.shape}")
    print(f"CoC data: {coc_df.shape}")
    
    # Convert homeless data to long format
    homeless_long = pd.melt(homeless_df, 
                           id_vars=['State'], 
                           var_name='Year', 
                           value_name='Homeless_Rate')
    homeless_long['Year'] = homeless_long['Year'].astype(int)
    
    # Prepare climate data
    climate_clean = climate_df[['Name', 'Year', 'Value']].copy()
    climate_clean.columns = ['State', 'Year', 'Temperature']
    
    # Create reverse state mapping (full name to abbreviation)
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
        'WISCONSIN': 'WI', 'WYOMING': 'WY'
    }
    
    # Also create mapping for title case state names
    title_state_mapping = {k.title(): v for k, v in state_mapping.items()}
    
    # Standardize state names
    climate_clean['State'] = climate_clean['State'].map(title_state_mapping)
    political_df['State'] = political_df['State'].map(state_mapping)  # Use uppercase mapping for political data
    
    print("\nSample of state formats after standardization:")
    print("Homeless:", homeless_long['State'].iloc[0])
    print("Climate:", climate_clean['State'].iloc[0])
    print("Political:", political_df['State'].iloc[0])
    print("CoC:", coc_df['State'].iloc[0])
    
    # Print unique states to verify standardization
    print("\nUnique states after standardization:")
    print("Homeless:", sorted(homeless_long['State'].unique()))
    print("Climate:", sorted(climate_clean['State'].unique()))
    print("Political:", sorted(political_df['State'].unique()))
    print("CoC:", sorted(coc_df['State'].unique()))
    
    # Merge datasets
    print("\nMerging datasets...")
    merged_df = pd.merge(homeless_long, climate_clean, on=['State', 'Year'])
    print(f"After homeless-climate merge: {merged_df.shape}")
    print("Sample after first merge:")
    print(merged_df.head())
    
    merged_df = pd.merge(merged_df, political_df, on=['State', 'Year'])
    print(f"\nAfter adding political data: {merged_df.shape}")
    print("Sample after second merge:")
    print(merged_df.head())
    
    merged_df = pd.merge(merged_df, coc_df[['State', 'Year', 'CoCs_per_hundredthousands']], 
                        on=['State', 'Year'])
    print(f"\nFinal shape: {merged_df.shape}")
    print("Final sample:")
    print(merged_df.head())
    
    # Calculate correlations
    if not merged_df.empty:
        correlations = merged_df[['Homeless_Rate', 'Temperature', 'Political_Index', 'CoCs_per_hundredthousands']].corr()
        
        # Plot correlation matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlations, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Matrix')
        plt.show()
    
    return merged_df

def run_multiple_models(X, y):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Initialize models
    models = {
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(random_state=42),
        'XGBoost': xgb.XGBRegressor(random_state=42)
    }
    
    results = {}
    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        
        # Calculate metrics
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        
        # Feature importance
        if hasattr(model, 'feature_importances_'):
            importance = pd.DataFrame({
                'feature': X.columns,
                'importance': model.feature_importances_
            }).sort_values('importance', ascending=False)
            
            # Plot feature importance
            plt.figure(figsize=(10, 5))
            sns.barplot(data=importance, x='feature', y='importance')
            plt.title(f'Feature Importance - {name}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        
        results[name] = {
            'R2': r2,
            'RMSE': rmse,
            'Feature_Importance': importance if 'importance' in locals() else None
        }
        
        print(f"R2 Score: {r2:.4f}")
        print(f"RMSE: {rmse:.4f}")
    
    return results

def main():
    # Prepare data
    print("Preparing data...")
    merged_df = prepare_data()
    
    if merged_df.empty:
        print("Error: No data after merging")
        return
    
    # Basic statistics
    print("\nBasic Statistics:")
    print(merged_df.describe())
    
    # Prepare features
    features = ['Temperature', 'Political_Index', 'CoCs_per_hundredthousands']
    X = merged_df[features]
    y = merged_df['Homeless_Rate']
    
    # Run models
    print("\nRunning models...")
    model_results = run_multiple_models(X, y)
    
    # Save results
    output_path = r"C:\Users\mhyles\Downloads\2024 Projects\NEREUS\model_results.csv"
    pd.DataFrame(model_results).T.to_csv(output_path)
    print(f"\nResults saved to: {output_path}")

if __name__ == "__main__":
    main()