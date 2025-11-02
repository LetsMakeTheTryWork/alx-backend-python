#!/usr/bin/python3
"""
0-stream_users.py
Creates a generator that streams rows from the user_data table
"""

import mysql.connector

def stream_users():
    """Generator that yields rows from the user_data table one by one."""
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",      # Replace with your MySQL username
        password="",      # Replace with your MySQL password
        database="ALX_prodev"
    )

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    # Use a single loop to yield each row
    for row in cursor:
        yield row

    # Clean up
    cursor.close()
    conn.close()
