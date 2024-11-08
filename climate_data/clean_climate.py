import pandas as pd
import os

# Set the directory path
directory = r"C:\Users\mhyles\Downloads\2024 Projects\homelessness\climate_data"

# Create an empty list to store dataframes
dfs = []

# Loop through files data to data (12)
for i in range(13):  # 0 to 12
    # Construct filename
    if i == 0:
        filename = "data.csv"
    else:
        filename = f"data ({i}).csv"
    
    file_path = os.path.join(directory, filename)
    
    try:
        # Skip the first 4 rows (metadata) and use row 5 as headers
        df = pd.read_csv(file_path, 
                        skiprows=4,
                        dtype={'ID': int, 
                              'Value': float, 
                              'Anomaly (1901-2000 base period)': float,
                              'Rank': int, 
                              '1901-2000 Mean': float})
        
        # Add year column (2010 + i)
        df['Year'] = 2010 + i
        
        # Print debugging information
        print(f"Successfully processed {filename}")
        print(f"Columns: {df.columns.tolist()}")
        print(f"First few rows:\n{df.head()}\n")
        
        # Append to list of dataframes
        dfs.append(df)
        
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {str(e)}")

if dfs:
    # Combine all dataframes
    combined_df = pd.concat(dfs, ignore_index=True)

    # Sort by Year and State ID
    combined_df = combined_df.sort_values(['Year', 'ID'])

    # Save combined dataset
    output_path = os.path.join(directory, 'combined_climate_data_2010_2022.csv')
    combined_df.to_csv(output_path, index=False)

    print("\nSummary:")
    print(f"Total rows: {len(combined_df)}")
    print(f"Years covered: {sorted(combined_df['Year'].unique())}")
    print(f"States covered: {len(combined_df['ID'].unique())}")
    print(f"\nSample of combined data:")
    print(combined_df.head())
    print(f"\nData saved to: {output_path}")

    # Verify completeness
    year_counts = combined_df.groupby('Year').size()
    print("\nRows per year:")
    print(year_counts)
    
    # Verify all states are present for each year
    state_year_counts = combined_df.groupby(['Year', 'ID']).size().unstack()
    print("\nMissing state-year combinations:")
    print(state_year_counts.isnull().sum().sum())
else:
    print("No data frames were successfully created.")