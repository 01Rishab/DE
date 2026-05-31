import duckdb
import pandas as pd
import random
from datetime import datetime, timedelta

# Connect to DuckDB (creates ecommerce.duckdb file)
con = duckdb.connect("ecommerce.duckdb")

# ── Generate fake e-commerce data ──────────────────────────────

random.seed(42)

# Customers
customers = pd.DataFrame({
    "customer_id": range(1, 201),
    "name": [f"Customer_{i}" for i in range(1, 201)],
    "email": [f"customer_{i}@email.com" for i in range(1, 201)],
    "city": random.choices(["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"], k=200),
    "signup_date": [
        (datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))).date()
        for _ in range(200)
    ]
})

# Products
products = pd.DataFrame({
    "product_id": range(1, 51),
    "name": [f"Product_{i}" for i in range(1, 51)],
    "category": random.choices(["Electronics", "Clothing", "Food", "Books", "Sports"], k=50),
    "price": [round(random.uniform(10, 500), 2) for _ in range(50)]
})

# Orders
orders = pd.DataFrame({
    "order_id": range(1, 1001),
    "customer_id": random.choices(range(1, 201), k=1000),
    "product_id": random.choices(range(1, 51), k=1000),
    "quantity": random.choices(range(1, 6), k=1000),
    "status": random.choices(["completed", "cancelled", "returned"], weights=[7, 2, 1], k=1000),
    "order_date": [
        (datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))).date()
        for _ in range(1000)
    ]
})

# ── Load into DuckDB ───────────────────────────────────────────

con.execute("CREATE SCHEMA IF NOT EXISTS raw")
con.execute("DROP TABLE IF EXISTS raw.customers")
con.execute("DROP TABLE IF EXISTS raw.products")
con.execute("DROP TABLE IF EXISTS raw.orders")

con.execute("CREATE TABLE raw.customers AS SELECT * FROM customers")
con.execute("CREATE TABLE raw.products AS SELECT * FROM products")
con.execute("CREATE TABLE raw.orders AS SELECT * FROM orders")

print("✅ Raw data loaded into DuckDB!")
print(f"   customers : {len(customers)} rows")
print(f"   products  : {len(products)} rows")
print(f"   orders    : {len(orders)} rows")

con.close()