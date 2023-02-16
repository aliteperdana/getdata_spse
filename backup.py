#!/usr/bin/python
import psycopg2
import time
import subprocess
from config import config

""" Backup Database Start """

# read connection parameters
params = config()

# Set the database connection parameters
host = params['host']
database = params['database']
user = params['user']
password = params['user']

# Set the backup file name
current_time = time.strftime('%Y-%m-%d %H-%M-%S')
backup_file = "backup_file/database_backup-"+current_time+".sql"

# Run the pg_dump command to create the backup
subprocess.run(
    ["pg_dump", "-h", host, "-d", database, "-U", user, "-f", backup_file],
    input=password.encode(),
    check=True
)

print("Database backup created successfully")
