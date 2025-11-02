#!/usr/bin/python3
"""
2-lazy_paginate.py
Lazy pagination generator for user_data
"""

seed = **import**('seed')

def paginate_users(page_size, offset):
"""Fetch a page of users from the database."""
connection = seed.connect_to_prodev()
cursor = connection.cursor(dictionary=True)
cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
rows = cursor.fetchall()
connection.close()
return rows

def lazy_pagination(page_size):
"""Generator that lazily fetches each page of users."""
offset = 0
while True:  # loop 1
page = paginate_users(page_size, offset)
if not page:
break
yield page
offset += page_size
