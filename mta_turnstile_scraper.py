#!/usr/bin/python3

"""
Scrapes latest data from the MTA Turnstile info 
(http://web.mta.info/developers/turnstile.html)
and dumps it into a given database

Usage: python mta_turnsite_scraper.py <db>
"""

import sqlite3

"""
Given a turnstile data file, parse data and dump into database
"""
def parse_file(file):
    return

"""
Set up database
"""
def init_db(database):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    return
