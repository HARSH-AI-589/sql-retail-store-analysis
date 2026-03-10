import sqlite3

# connect to database
conn = sqlite3.connect("retail_store.db")

# create cursor
cursor = conn.cursor()

print("Database connected")
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER,
    name TEXT,
    city TEXT,
    age INTEGER
)
""")

conn.commit()

print("Customers table created")
cursor.execute("""
INSERT INTO customers VALUES
(1, 'John', 'New York', 30),
(2, 'Emma', 'Chicago', 25),
(3, 'David', 'Boston', 40),
(4, 'Sophia', 'Seattle', 29),
(5, 'Michael', 'Austin', 35)
""")

conn.commit()

print("Customer data inserted")
cursor.execute("SELECT * FROM customers")

rows = cursor.fetchall()

for row in rows:
    print(row)
    cursor.execute("SELECT * FROM customers WHERE age > 30")

results = cursor.fetchall()

print("Customers older than 30:")

for r in results:
    print(r)
    cursor.execute("SELECT COUNT(*) FROM customers")

total = cursor.fetchone()

print("Total number of customers:", total[0])
cursor.execute("SELECT AVG(age) FROM customers")

avg_age = cursor.fetchone()

print("Average age of customers:", avg_age[0])
cursor.execute("SELECT * FROM customers ORDER BY age")

sorted_data = cursor.fetchall()

print("Customers sorted by age:")

for s in sorted_data:
    print(s)
    cursor.execute("SELECT MAX(age) FROM customers")

oldest = cursor.fetchone()

print("Oldest customer age:", oldest[0])
cursor.execute("SELECT MIN(age) FROM customers")

youngest = cursor.fetchone()

print("Youngest customer age:", youngest[0])
cursor.execute("""
SELECT city, COUNT(*)
FROM customers
GROUP BY city
""")

city_data = cursor.fetchall()

print("Customers in each city:")

for c in city_data:
    print(c)
    cursor.execute("""
SELECT city, COUNT(*)
FROM customers
GROUP BY city
HAVING COUNT(*) > 1
""")

result = cursor.fetchall()

print("Cities with more than 1 customer:")

for r in result:
    print(r)
    cursor.execute("""
UPDATE customers
SET age = 26
WHERE name = 'Emma'
""")

conn.commit()

print("Customer age updated")
cursor.execute("""
DELETE FROM customers
WHERE name = 'Michael'
""")

conn.commit()

print("Customer deleted")