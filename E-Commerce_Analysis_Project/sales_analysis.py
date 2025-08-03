import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a professional style for the plots
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6) # Default figure size

# Load the dataset
try:
    df = pd.read_csv('sales_data.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'sales_data.csv' not found. Please make sure the file is in the same directory.")
    exit()

# Display basic information about the dataset
print("\nFirst 5 rows of the dataset:")
print(df.head())
print("\nDataFrame Info:")
df.info()
print("\nDescriptive Statistics:")
print(df.describe())

# --- Data Visualization ---

# Convert 'OrderDate' to datetime objects
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# 1. Monthly Total Sales Chart
df['Month'] = df['OrderDate'].dt.month
monthly_sales = df.groupby('Month')['TotalAmount'].sum()
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color='b')
plt.title('Monthly Total Sales for 2024', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales (TL)', fontsize=12)
plt.xticks(range(1, 13))
plt.grid(True)
plt.savefig('monthly_sales_chart.png')
plt.show()

# 2. Total Sales by Product Category Chart
category_sales = df.groupby('ProductCategory')['TotalAmount'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=category_sales.index, y=category_sales.values, palette='viridis')
plt.title('Total Sales by Product Category', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales (TL)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('category_sales_chart.png')
plt.show()

# 3. Customer Age Distribution Chart
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='purple')
plt.title('Customer Age Distribution', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.tight_layout()
plt.savefig('age_distribution_chart.png')
plt.show()

print("\nAll charts have been generated and saved to your project folder.")