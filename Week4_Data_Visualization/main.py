import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('sales_data.csv')

# Display first rows
print("===== FIRST 5 ROWS =====")
print(df.head())

# Dataset info
print("\n===== DATASET INFO =====")
print(df.info())

# Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Total sales calculation
df['Total_Sales'] = df['Quantity'] * df['Price']

# Basic metrics
total_revenue = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()
highest_sales = df['Total_Sales'].max()

print("\n===== SALES REPORT =====")
print(f"Total Revenue: ₹{total_revenue}")
print(f"Average Sales: ₹{average_sales:.2f}")
print(f"Highest Sale: ₹{highest_sales}")

# Sales by product
sales_by_product = df.groupby('Product')['Total_Sales'].sum()

# ---------------- BAR CHART ----------------
plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar')

plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')

plt.tight_layout()
plt.savefig('visualizations/bar_chart.png')
plt.show()

# ---------------- LINE CHART ----------------
plt.figure(figsize=(8,5))

df['Total_Sales'].plot(kind='line')

plt.title('Sales Trend')
plt.xlabel('Index')
plt.ylabel('Sales')

plt.tight_layout()
plt.savefig('visualizations/line_chart.png')
plt.show()

# ---------------- PIE CHART ----------------
plt.figure(figsize=(7,7))

sales_by_product.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title('Sales Distribution')

plt.ylabel('')

plt.tight_layout()
plt.savefig('visualizations/pie_chart.png')
plt.show()

print("\nCharts saved in visualizations folder.")