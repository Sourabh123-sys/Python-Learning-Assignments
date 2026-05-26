import pandas as pd

# Load dataset
df = pd.read_csv('Week3_Data_Analysis/amazon.csv')

# Display first 5 rows
print("===== FIRST 5 ROWS =====")
print(df.head())

# Dataset information
print("\n===== DATASET INFO =====")
print(df.info())

# Shape of dataset
print("\nRows and Columns:")
print(df.shape)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Remove ₹ and commas from price columns
df['discounted_price'] = df['discounted_price'].str.replace('₹', '')
df['discounted_price'] = df['discounted_price'].str.replace(',', '')
df['discounted_price'] = df['discounted_price'].astype(float)

df['actual_price'] = df['actual_price'].str.replace('₹', '')
df['actual_price'] = df['actual_price'].str.replace(',', '')
df['actual_price'] = df['actual_price'].astype(float)

# Convert rating column
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Basic Analysis
average_rating = df['rating'].mean()
highest_price = df['actual_price'].max()
lowest_price = df['actual_price'].min()

# Most expensive product
most_expensive = df.loc[df['actual_price'].idxmax(), 'product_name']

# Cheapest product
cheapest = df.loc[df['actual_price'].idxmin(), 'product_name']

# Report
print("\n===== AMAZON DATA ANALYSIS REPORT =====")
print(f"Average Product Rating: {average_rating:.2f}")
print(f"Highest Product Price: ₹{highest_price}")
print(f"Lowest Product Price: ₹{lowest_price}")
print(f"Most Expensive Product: {most_expensive}")
print(f"Cheapest Product: {cheapest}")