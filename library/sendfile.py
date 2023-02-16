#!/usr/bin/python
import requests
from config import endpoint

def send(key,file,file_name):
    #read env file endpoint section
    endpoints = endpoint()

    #Prepare Endpoint And Key
    url = endpoints['host']+'/'+key
    headers = {
        'key': endpoints['key']
    }
    files = open(file,'rb')

    #Send Request
    request = requests.post(url, headers=headers, files={'file': (file_name,files, 'application/zip')})

    #Read Response
    response = request.json()
    return response

def check_process(process_id):
    endpoints = endpoint()
    url = url = endpoints['host']+'/check_process/'+process_id
    headers = {
        'key': endpoints['key']
    }
    response = requests.post(url,headers=headers)
    data = response.json()
    return data
    

def TestConnection():
    endpoints = endpoint()
    url = url = endpoints['host']+'/test'
    headers = {
        'key': endpoints['key']
    }
    response = requests.get(url,headers=headers)
    data = response.json()
    print(data)
