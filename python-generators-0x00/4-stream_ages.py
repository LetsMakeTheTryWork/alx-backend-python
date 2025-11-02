#!/usr/bin/python3
"""
4-stream_ages.py
Memory-efficient computation of average user age using a generator
"""

import mysql.connector

def stream_user_ages():
"""Generator that yields user ages one by one from the database."""
conn = mysql.connector.connect(
host="localhost",
user="root",        # Replace with your MySQL username
password="",        # Replace with your MySQL password
database="ALX_prodev"
)
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT age FROM user_data")

```
for row in cursor:  # loop 1
    yield row['age']

cursor.close()
conn.close()
```

def compute_average_age():
"""Compute the average age using the generator without loading all data."""
total = 0
count = 0
for age in stream_user_ages():  # loop 2
total += age
count += 1
average = total / count if count else 0
print(f"Average age of users: {average:.2f}")

if **name** == "**main**":
compute_average_age()
