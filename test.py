import psycopg2
import json
from decimal import Decimal
from datetime import datetime

# Connect to the database
conn = psycopg2.connect(
    host="10.250.10.55",
    database="epns_prod",
    user="postgres",
    password="postgres"
)

# Create a cursor
cur = conn.cursor()

# Execute a SELECT statement with a WHERE clause
cur.execute("SELECT * FROM pemilik WHERE date_trunc('year', auditupdate) = '2022-01-01'")

# Fetch the results of the SELECT statement
rows = cur.fetchall()

# Convert the results to a list of dictionaries
data = []
for row in rows:
    data_row = {}
    for i, column in enumerate(row):
        if isinstance(column, Decimal):
            data_row[cur.description[i][0]] = str(column)
        elif isinstance(column, datetime):
            data_row[cur.description[i][0]] = column.strftime('%Y-%m-%d %H:%M:%S')
        else:
            data_row[cur.description[i][0]] = column
    data.append(data_row)

# Write the data to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Close the cursor
cur.close()

# Close the connection
conn.close()