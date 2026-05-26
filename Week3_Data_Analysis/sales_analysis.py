# Import pandas library
import pandas as pd

# Load CSV file
df = pd.read_csv('Week3_Data_Analysis/sales_data.csv')

print("SALES DATA")
print(df.head())

# Dataset Information
print("\nDATASET INFO")

# Number of rows and columns
print("Shape of dataset:", df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Check Missing Values
print("\nMISSING VALUES")

print(df.isnull().sum())

# Fill missing values with 0
df.fillna(0, inplace=True)

# Remove Duplicate Rows
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Sales Analysis
print("\nSALES ANALYSIS")

# Total sales/revenue
total_sales = df['Total_Sales'].sum()

print(f"Total Revenue: ₹{total_sales:,.2f}")

# Average sales
average_sales = df['Total_Sales'].mean()

print(f"Average Sales: ₹{average_sales:,.2f}")

# Highest sales
highest_sales = df['Total_Sales'].max()

print(f"Highest Sale: ₹{highest_sales:,.2f}")

# Lowest sales
lowest_sales = df['Total_Sales'].min()

print(f"Lowest Sale: ₹{lowest_sales:,.2f}")

# Best Selling Product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

best_product_sales = df.groupby('Product')['Total_Sales'].sum().max()

print("\nBest Selling Product:", best_product)

print(f"Sales Generated: ₹{best_product_sales:,.2f}")

# Final Report
print("\nFINAL REPORT")

print(f"""
Sales Data Analysis Report

Total Revenue      : ₹{total_sales:,.2f}
Average Sales      : ₹{average_sales:,.2f}
Highest Sale       : ₹{highest_sales:,.2f}
Lowest Sale        : ₹{lowest_sales:,.2f}
Best Selling Item  : {best_product}
Best Product Sales : ₹{best_product_sales:,.2f}
""")

print("Analysis Completed Successfully!")