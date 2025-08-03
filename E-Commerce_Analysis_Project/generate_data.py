import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker with Turkish locale for more realistic data
fake = Faker('tr_TR')

def generate_sales_data(num_rows):
    # Lists and ranges for realistic data
    product_categories = ['Electronics', 'Clothing', 'Home & Garden', 'Beauty', 'Books', 'Toys']
    cities = ['Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Antalya', 'Adana', 'Konya']
    payment_methods = ['Credit Card', 'Wire Transfer', 'Cash on Delivery']

    # Generate random dates for the year 2024
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    dates = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(num_rows)]

    data = {
        'OrderID': range(1001, 1001 + num_rows),
        'OrderDate': [d.strftime('%Y-%m-%d') for d in dates],
        'CustomerID': [random.randint(20000, 30000) for _ in range(num_rows)],
        'FirstName': [fake.first_name() for _ in range(num_rows)],
        'LastName': [fake.last_name() for _ in range(num_rows)],
        'Email': [fake.email() for _ in range(num_rows)],
        'Gender': [random.choice(['Male', 'Female']) for _ in range(num_rows)],
        'Age': [random.randint(18, 65) for _ in range(num_rows)],
        'City': [random.choice(cities) for _ in range(num_rows)],
        'ProductCode': [f'PRD-{random.randint(100, 999)}' for _ in range(num_rows)],
        'ProductCategory': [random.choice(product_categories) for _ in range(num_rows)],
        'UnitPrice': [round(random.uniform(25.0, 5000.0), 2) for _ in range(num_rows)],
        'Quantity': [random.randint(1, 5) for _ in range(num_rows)],
    }
    
    df = pd.DataFrame(data)
    df['TotalAmount'] = df['UnitPrice'] * df['Quantity']

    def get_payment_method(total_amount):
        if total_amount > 1000:
            return random.choice(['Credit Card', 'Wire Transfer'])
        else:
            return random.choice(payment_methods)
            
    df['PaymentMethod'] = df['TotalAmount'].apply(get_payment_method)
    return df

# Generate a dataset with 2000 rows
num_rows = 2000
sales_df = generate_sales_data(num_rows)

print("First 5 rows of the generated dataset:")
print(sales_df.head())

# Save the DataFrame to a CSV file
sales_df.to_csv('sales_data.csv', index=False, encoding='utf-8')
print(f"\nA dataset with '{num_rows}' rows has been saved as 'sales_data.csv'.")