"""
Gets links and content to all turnstile files
from http://web.mta.info/developers/turnstile.html
"""

import re
import urllib.request as request
from datetime import datetime
from util import trace
from bs4 import BeautifulSoup

MTA_TURNSTILE_URL = "http://web.mta.info/developers/turnstile.html"
MTA_FILE_ROOT_URL = "http://web.mta.info/developers/"

"""
Get links
"""
def get_site():
    f = request.urlopen(MTA_TURNSTILE_URL)
    content = f.read()
    return content

def get_turnstile_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    turnstile_links = [(link.text, MTA_FILE_ROOT_URL + link['href']) for link in links if re.match('.*day.*20..', link.text)]
    return turnstile_links 

def get_links_by_date(start, end):
    links = get_links()
    in_range = []
    for text,link in links:
        date = datetime.strptime(text , "%A, %B %d, %Y") 
        if date >= start and date <= end:
            in_range.append((text, link))
    
    return in_range

def get_links():
    return get_turnstile_links(get_site())

def test():
    content = get_site()
    links = get_turnstile_links(content)
    assert len(links) == 282 #legit as of 30 Sept 2015

    r = get_links_by_date(datetime(2015, 8, 1), datetime(2015, 8, 31))
    assert len(r) == 5 # 5 entries for August 2015 

    s = get_links_by_date(datetime(2013, 4, 6), datetime(2013, 4, 27))
    assert len(s) == 4 # test edge case

    trace('test pass')
