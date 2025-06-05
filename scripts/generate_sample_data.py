import pandas as pd
import os 

# Sample data as a list of dictionaries

data = [
    {"transaction_id": 1001, "store_id": "S001", "product_id": "P100", "sale_date": "2023-01-01", "quantity": 2, "price": 150.00},
    {"transaction_id": 1002, "store_id": "S001", "product_id": "P101", "sale_date": "2023-01-01", "quantity": 1, "price": 200.00},
    {"transaction_id": 1003, "store_id": "S002", "product_id": "P100", "sale_date": "2023-01-02", "quantity": 3, "price": 150.00},
    {"transaction_id": 1004, "store_id": "S002", "product_id": "P102", "sale_date": "2023-01-02", "quantity": 2, "price": 300.00},
    {"transaction_id": 1005, "store_id": "S003", "product_id": "P103", "sale_date": "2023-01-03", "quantity": 1, "price": 450.00},
    {"transaction_id": 1006, "store_id": "S003", "product_id": "P101", "sale_date": "2023-01-03", "quantity": 2, "price": 200.00},
    {"transaction_id": 1007, "store_id": "S001", "product_id": "P102", "sale_date": "2023-01-04", "quantity": 1, "price": 300.00},
    {"transaction_id": 1008, "store_id": "S002", "product_id": "P103", "sale_date": "2023-01-04", "quantity": 2, "price": 450.00},
]

# Create DataFrame 

df = pd.DataFrame(data)

# Ensure that data folder exists

os.makedirs("data", exist_ok=True)

# Save to CSV

df.to_csv("data/sales.csv", index = False)

print("sales.csv saved in data")