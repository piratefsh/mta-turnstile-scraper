#!/usr/bin/python3

"""
Scrapes latest data from the MTA Turnstile info 
(http://web.mta.info/developers/turnstile.html)
and dumps it into a given database

Usage: python mta_turnsite_scraper.py <db>
"""

import sqlite3

# Globals
# Columns
COLUMN_HEADERS = "CA,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS".split(',') 
COLUMN_DATATYPES = "TEXT,TEXT,TEXT,TEXT,TEXT,TEXT,DATE,TIME,TEXT,INTEGER,INTEGER".split(',')

"""
Given a turnstile data file, parse data and dump into database
"""
def parse_file(file):
    return

"""
Set up database
"""
def init_db(database):
    # Queries
    header_and_datatypes = ", ".join([COLUMN_HEADERS[i] + ' ' + COLUMN_DATATYPES[i] for i in range(len(COLUMN_HEADERS))])
    
    print(header_and_datatypes)
    
    Q = {
        'create' : 'CREATE TABLE IF NOT EXISTS entries (' + header_and_datatypes + ')'
    }
    print(Q['create'])
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(Q['create'])
    return
