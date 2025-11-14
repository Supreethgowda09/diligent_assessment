import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

tables = ["customers", "products", "orders", "order_items", "payments"]
for t in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {t}")

cursor.execute("""
CREATE TABLE customers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    city TEXT
);
""")
cursor.execute("""
CREATE TABLE products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
);
""")
cursor.execute("""
CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT
);
""")
cursor.execute("""
CREATE TABLE order_items(
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER
);
""")
cursor.execute("""
CREATE TABLE payments(
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    payment_method TEXT,
    amount REAL,
    status TEXT
);
""")

def load_csv(csv, table):
    df = pd.read_csv(f"data/{csv}")
    df.to_sql(table, conn, if_exists="append", index=False)
    print(f"Inserted {table}")

load_csv("customers.csv", "customers")
load_csv("products.csv", "products")
load_csv("orders.csv", "orders")
load_csv("order_items.csv", "order_items")
load_csv("payments.csv", "payments")

conn.commit()
conn.close()
print("Database created successfully!")
