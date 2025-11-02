

This Python project sets up a MySQL database called `ALX_prodev` and populates it with user data from a CSV file. The script creates a `user_data` table with a UUID primary key and fields for name, email, and age.

## Features

* Connects to a MySQL server
* Creates a database `ALX_prodev` if it does not exist
* Creates a table `user_data` with the following fields:

  * `user_id` (Primary Key, UUID, Indexed)
  * `name` (VARCHAR, NOT NULL)
  * `email` (VARCHAR, NOT NULL)
  * `age` (DECIMAL, NOT NULL)
* Inserts data from `user_data.csv` without duplicating existing records

## Example Output

When running the script (`./0-main.py`), you should see:

```
faithokoth@ubuntu:python-generators-0x00 % ./0-main.py
connection successful
Table user_data created successfully
Database ALX_prodev is present
[('00234e50-34eb-4ce2-94ec-26e3fa749796', 'Dan Altenwerth Jr.', 'Molly59@gmail.com', 67),
 ('006bfede-724d-4cdd-a2a6-59700f40d0da', 'Glenda Wisozk', 'Miriam21@gmail.com', 119),
 ('006e1f7f-90c2-45ad-8c1d-1275d594cc88', 'Daniel Fahey IV', 'Delia.Lesch11@hotmail.com', 49),
 ('00af05c9-0a86-419e-8c2d-5fb7e899ae1c', 'Ronnie Bechtelar', 'Sandra19@yahoo.com', 22),
 ('00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4', 'Alma Bechtelar', 'Shelly_Balistreri22@hotmail.com', 102)]
```

## Requirements

* Python 3.x
* MySQL server
* Python packages:

  * `mysql-connector-python`

Install the required package using pip:

```bash
pip install mysql-connector-python
```

## Usage

1. Place `user_data.csv` in the project folder.
2. Update MySQL credentials in `seed.py`:

```python
user="root"          # Replace with your MySQL username
password=""          # Replace with your MySQL password
```

3. Run the main script:

```bash
./0-main.py
```

This will:

* Connect to MySQL
* Create the `ALX_prodev` database
* Create the `user_data` table
* Insert CSV data
* Display confirmation and first 5 rows from the table

## CSV Format

The CSV file should have the following headers:

```
name,email,age
```

Example (`user_data.csv`):

```
John Doe,john@example.com,30
Jane Smith,jane@example.com,25
```

## Notes

* Each record is assigned a unique UUID.
* Duplicate emails are not inserted.
* Ensure your MySQL server is running and accessible.

## License

This project is open-source and free to use.
