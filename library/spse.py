#!/usr/bin/python
import psycopg2
import json
import time
import datetime
import csv
import os
import pandas as pd
import zipfile
import gzip
from config import config
from library.sendfile import send
from library.sendfile import check_process

def spse(nm_table):
    conn = None
    current_time = time.strftime('%Y-%m-%d_%H-%M-%S')
    table = nm_table

    # read connection parameters
    params = config()

    # connect to the PostgreSQL server
    # print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)
    
    # create a cursor
    cur = conn.cursor()

    # Create File Name
    file_name = table+'-'+current_time

    # Create Directory
    directory = "file/"+file_name
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Full PATH for CSV FILE Name
    full_path_csv = 'file/'+file_name+'/'+file_name+'.csv'


    # Use the COPY command to export the data from the table to a file
    with open(full_path_csv, 'w') as f:
        cur.copy_expert("COPY "+table+" TO STDOUT WITH (FORMAT CSV, HEADER TRUE)", f)

    
    # Close the cursor and connection
    cur.close()
    conn.close()

    # Split CSV 
    for i, chunk in enumerate(pd.read_csv(full_path_csv, chunksize=1000)):
        json_file_name = f"{full_path_csv.split('.')[0]}_{i+1}_part.json.gz"
        json_data = chunk.to_json(orient='records')
        with gzip.open(json_file_name, "w") as gz_file:
            gz_file.write(json_data.encode())


    # ZIP ALL FILE JSON Into Single Archive
    folder_name = 'file/'+file_name
    zip_file_name = f"{full_path_csv.split('.')[0]}.zip"

    with zipfile.ZipFile(zip_file_name, mode='w') as zf:
        for file in os.listdir(folder_name):
            if file.endswith('.json.gz'):
                zf.write(os.path.join(folder_name, file),arcname=file)

    
    # Delete all split file
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            if file.endswith('json.gz'):
                os.remove(os.path.join(root,file))
    
    # Send Data To API
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengirim Data Ke API")
    time.sleep(1)

    file_name_and_ext = file_name+'.zip'
    response = send(nm_table,zip_file_name,file_name_and_ext)

    # Check Input If Success
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Data Telah Dikirim Ke API")

    process_id = response['process_id']
    response_process = check_process(process_id)
    
    # Check If Progress Success
    while(response_process['progress']!= 100):
        time.sleep(10)
        response_process = check_process(process_id)

    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Data Berhasil Ditambahkan")
    
    print("------------------")
    




