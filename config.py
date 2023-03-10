#!/usr/bin/python
from configparser import ConfigParser

file_config = ".env"

def config(filename=file_config, section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def endpoint(filename=file_config, section='endpoint'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section
    endpoint = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            endpoint[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return endpoint