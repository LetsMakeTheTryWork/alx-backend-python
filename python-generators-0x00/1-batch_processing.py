#!/usr/bin/python3
"""
1-batch_processing.py
Batch processing generator for user_data
"""

import mysql.connector

def stream_users_in_batches(batch_size):
conn = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="ALX_prodev"
)
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM user_data")

```
batch = []
for row in cursor:
    batch.append(row)
    if len(batch) == batch_size:
        yield batch
        batch = []

if batch:
    yield batch

cursor.close()
conn.close()
```



def batch_processing(batch_size):
for batch in stream_users_in_batches(batch_size):
for user in (u for u in batch if u['age'] > 25):
yield user
