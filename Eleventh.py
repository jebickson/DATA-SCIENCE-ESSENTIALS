import pandas as pd

# Load data from CSV files
sales_df = pd.read_csv(r'C:\Users\Happyy\Documents\salesdata.csv')
region_df = pd.read_csv(r'C:\Users\Happyy\Documents\Region.csv')  # ✅ Corrected variable name

# Display the loaded DataFrames
print("Sales Data:")
print(sales_df)
print("\nRegion Data:")
print(region_df)

# Strip whitespace from column names
sales_df.columns = sales_df.columns.str.strip()
region_df.columns = region_df.columns.str.strip()

# Optional: Ensure 'Date' is in datetime format
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# --------------------------------------------------
# 1. Combine DataFrames (Merge on 'Region')
# --------------------------------------------------
combined_df = pd.merge(sales_df, region_df, on='Region', how='inner')
print("\nCombined DataFrame (Merged on 'Region'):")
print(combined_df)

# --------------------------------------------------
# 2. Sorting DataFrame by 'Sales' and 'Date'
# --------------------------------------------------
sorted_df = combined_df.sort_values(by=['Sales', 'Date'], ascending=[False, True])
print("\nSorted DataFrame by 'Sales' (descending) and 'Date' (ascending):")
print(sorted_df)

# --------------------------------------------------
# 3. Reshaping DataFrame (Pivot)
# --------------------------------------------------
pivoted_df = combined_df.pivot(index='Date', columns='Region', values='Sales')
print("\nPivoted DataFrame (Sales by Date and Region):")
print(pivoted_df)

# --------------------------------------------------
# 4. Reshaping DataFrame (Melt)
# --------------------------------------------------
melted_df = pd.melt(combined_df, id_vars=['Date'], value_vars=['Sales'], var_name='Metric', value_name='Value')
print("\nMelted DataFrame (Sales Data in long Format):")
print(melted_df)
