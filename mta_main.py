#!/usr/bin/python3

"""
Main file to scrape links from turnstile listing 
and insert into given database
"""

import mta_db as db
import mta_scraper as scraper
import sys
from util import trace
from datetime import datetime
def main():
    dbname = ""
    start_date = datetime(2010, 5, 5)
    end_date = datetime.now()
    date_format = "%Y-%m-%d"

    if(len(sys.argv) == 4):
        dbname = sys.argv[1]
        start_date = datetime.strptime(sys.argv[2], date_format)
        end_date = datetime.strptime(sys.argv[3], date_format)
    else:
        print("Usage: mta_main.py <db name> <start date: YYYY-MM-DD> <end date: YYYY-MM-DD>")
        return

    # init db
    trace('initializing db:', dbname)
    db.init_db(dbname)
    
    # get links
    links = scraper.get_links_by_date(start_date, end_date)
    
    # for each link, do url_to_db
    for date,link in links:
        trace('loading file:', link)
        db.url_to_db(link)

    # check for accuracy
main()
