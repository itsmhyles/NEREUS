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


# Read and prepare data
homeless_df = pd.read_csv(homeless_file )
climate_df = pd.read_csv(climate_file)
political_df = pd.read_csv(political_file)

# Check data structures first
print("Homeless Data Structure:")
print(homeless_df.head())
print("\nColumns:", homeless_df.columns.tolist())

print("\nClimate Data Structure:")
print(climate_df.head())
print("\nColumns:", climate_df.columns.tolist())

print("\nPolitical Data Structure:")
print(political_df.head())
print("\nColumns:", political_df.columns.tolist())