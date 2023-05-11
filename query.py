import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")

# Create a cursor object
cursor = conn.cursor()

# Select the first three rows from the table
select_query = """
SELECT * FROM client_config LIMIT 8
"""
cursor.execute(select_query)
result = cursor.fetchall()
for row in result:
    print(row)

# Close the connection
conn.close()
