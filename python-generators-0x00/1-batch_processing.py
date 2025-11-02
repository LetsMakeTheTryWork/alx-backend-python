#!/usr/bin/python3
"""
1-batch_processing.py
Batch processing generator for user_data
"""

import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields rows from user_data in batches."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        # Replace with your MySQL username
        password="",        # Replace with your MySQL password
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    batch = []
    for row in cursor:  # loop 1
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch

    cursor.close()
    conn.close()

def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):  # loop 2
        for user in batch:  # loop 3
            if user['age'] > 25:
                print(user)
