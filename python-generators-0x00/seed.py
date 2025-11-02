import mysql.connector
import csv
import uuid

# MySQL credentials – replace with your credentials

MYSQL_HOST = "localhost"
MYSQL_USER = "root"      # Replace with your MySQL username
MYSQL_PASSWORD = ""      # Replace with your MySQL password
DB_NAME = "ALX_prodev"
TABLE_NAME = "user_data"

def connect_db():
"""Connect to the MySQL server"""
try:
connection = mysql.connector.connect(
host=MYSQL_HOST,
user=MYSQL_USER,
password=MYSQL_PASSWORD
)
return connection
except mysql.connector.Error as err:
print(f"Error connecting to MySQL server: {err}")
return None

def create_database(connection):
"""Create the ALX_prodev database if it does not exist"""
try:
cursor = connection.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
cursor.close()
except mysql.connector.Error as err:
print(f"Failed creating database: {err}")

def connect_to_prodev():
"""Connect to the ALX_prodev database"""
try:
connection = mysql.connector.connect(
host=MYSQL_HOST,
user=MYSQL_USER,
password=MYSQL_PASSWORD,
database=DB_NAME
)
return connection
except mysql.connector.Error as err:
print(f"Error connecting to {DB_NAME}: {err}")
return None

def create_table(connection):
"""Create the user_data table if it does not exist"""
try:
cursor = connection.cursor()
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
user_id CHAR(36) PRIMARY KEY,
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL UNIQUE,
age DECIMAL NOT NULL,
INDEX(user_id)
);
""")
connection.commit()
cursor.close()
print(f"Table {TABLE_NAME} created successfully")
except mysql.connector.Error as err:
print(f"Error creating table: {err}")

def insert_data(connection, csv_file):
"""Insert data from a CSV file if it does not exist"""
try:
cursor = connection.cursor()
with open(csv_file, newline='') as f:
reader = csv.DictReader(f)
for row in reader:
# Skip if email already exists
cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE email=%s", (row['email'],))
if cursor.fetchone():
continue
user_id = str(uuid.uuid4())
cursor.execute(f"""
INSERT INTO {TABLE_NAME} (user_id, name, email, age)
VALUES (%s, %s, %s, %s);
""", (user_id, row['name'], row['email'], row['age']))
connection.commit()
cursor.close()
print(f"Data inserted successfully from {csv_file}")
except mysql.connector.Error as err:
print(f"Error inserting data: {err}")
except FileNotFoundError:
print(f"CSV file '{csv_file}' not found")

if **name** == "**main**":
# Step 1: Connect to MySQL server
conn = connect_db()
if conn:
create_database(conn)
conn.close()

```
# Step 2: Connect to the newly created database
conn = connect_to_prodev()
if conn:
    create_table(conn)
    insert_data(conn, "user_data.csv")
    conn.close()