#!/usr/bin/python3

"""
Scrapes latest data from the MTA Turnstile info 
(http://web.mta.info/developers/turnstile.html)
and dumps it into a given database

Usage: python mta_turnsite_scraper.py <db>
"""

import sqlite3
import urllib.request as request
from util import trace

# Globals
# Columns
COLUMN_HEADERS = "CA,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS".split(',') 
COLUMN_DATATYPES = "TEXT,TEXT,TEXT,TEXT,TEXT,TEXT,DATE,TIME,TEXT,INTEGER,INTEGER".split(',')

# Database
DATABASE = 'test.db'
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

OVERRIDE_PROMPTS = False

"""
Given a turnstile data file, parse data and dump into database
"""
def file_to_db(filename):
    with open(filename) as f:
        next(f) # skip header
        for line in f:
            add_entry_db(line.strip())
    commit_db()
    return

"""
Given a file url, parse data and dump into db
"""
def url_to_db(url):
    with request.urlopen(url) as req:
        # handle two formats
        header = next(req).decode('utf-8')
        if header.count(',') > 10:
            # is old format
            # c/a, unit
            # scp, date, time, desc, entry, exit
            for line in req:
                line = line.decode('utf-8').strip()
                entries = convert_format(line)
                for l in entries:
                    add_entry_db(l)
        else:
            # is new format
            for line in req:
                line = line.decode('utf-8').strip()
                trace(line)
                if(len(line) > 1):
                    add_entry_db(line)
        commit_db()
        return

"""
Convert old line format to new
"""

def convert_format(line):
    parts = line.split(',')
    ca_and_unit = ",".join(parts[0:3])
    data = parts[3:]
    data_len = 5 
    entries = [data[i:i+data_len] for i in range(0, len(data), data_len)] 
    lines = []
    for entry in entries:
        date = entry[0]
        time = entry[1]
        desc = entry[2]
        entries = entry[3]
        exits = entry[4]
        reformat = ["STATION", "LINENAME", "DIVISION", date, time, desc, entries, exits] 
        l = ca_and_unit + ',' + ','.join(reformat) 
        lines.append(l)
    return lines


"""
Commit db entries
"""
def commit_db():
    connection.commit()
    return

"""
Given a line of entry from raw, add that entry to db without commiting
"""
def add_entry_db(line):
    # format values accordingly
    values = line.split(',')
    values.insert(0, None)
    values = tuple(values)
    placeholder = ",".join(['?']*(len(COLUMN_HEADERS)+1))
    insert_query = 'INSERT INTO entries VALUES(' + placeholder + ')'
    #trace(insert_query, values)
    cursor.execute(insert_query, values)
    return

"""
Clear all tables
"""
def clear_db():
    confirm = 'y'
    if not OVERRIDE_PROMPTS:
        confirm = input('Sure you wanna drop all tables?')
    if confirm is 'y': 
        cursor.execute('DROP TABLE IF EXISTS entries')
        commit_db()

"""
Set up database
"""
def init_db():
    # create headers for entries 

    header_and_datatypes = "id INTEGER PRIMARY KEY AUTOINCREMENT,  " + ", ".join([COLUMN_HEADERS[i] + ' ' + COLUMN_DATATYPES[i] for i in range(len(COLUMN_HEADERS))])
    create_query =  'CREATE TABLE IF NOT EXISTS entries (' + header_and_datatypes + ')' # create 'entries' table cursor.execute(create_query)
    return

def test():
    global OVERRIDE_PROMPTS 
    OVERRIDE_PROMPTS = True
    clear_db()


    init_db()
    add_entry_db('A002,R051,02-00-00,LEXINGTON AVE,NQR456,BMT,09/19/2015,00:00:00,REGULAR,0005317608,0001797091')
    commit_db()
    assert len(cursor.execute('SELECT * FROM entries WHERE CA=?', ('A002',)).fetchall()) == 1
    
    # test file
    clear_db()
    init_db()
    file_to_db('turnstile_150926.txt')
    num_entries = len(cursor.execute('SELECT * FROM entries').fetchall())
    assert num_entries == 194625 
    
    # test url
    clear_db()
    init_db()
    url_to_db('http://web.mta.info/developers/data/nyct/turnstile/turnstile_150926.txt')
    num_entries = len(cursor.execute('SELECT * FROM entries').fetchall())
    assert num_entries == 194625 

    OVERRIDE_PROMPTS = False

    trace('tests pass')


def test_util():
    # test conversion
    old = "A022,R022,01-00-01,04-23-10,04:00:00,RECOVR,012277581,004593025,04-23-10,08:00:00,AUD,012277627,004593158,04-23-10,12:00:00,REGULAR,012278037,004593983,04-23-10,16:00:00,REGULAR,012279285,004594519,04-23-10,20:00:00,REGULAR,012281573,004594935"

    converted = convert_format(old)
    assert converted[0] == "A022,R022,01-00-01,STATION,LINENAME,DIVISION,04-23-10,04:00:00,RECOVR,012277581,004593025"
    assert converted[2] == "A022,R022,01-00-01,STATION,LINENAME,DIVISION,04-23-10,12:00:00,REGULAR,012278037,004593983"
    
    trace('tests pass')
