"""
Gets links and content to all turnstile files
from http://web.mta.info/developers/turnstile.html
"""

import re
import urllib.request as request
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
    turnstile_links = [MTA_FILE_ROOT_URL + link['href'] for link in links if re.match('Saturday.*20..', link.text)]
    return turnstile_links 

def get_links():
    return get_turnstile_links(get_site())

def test():
    content = get_site()
    links = get_turnstile_links(content)
    trace(links)
    assert len(links) == 280 #legit as of 30 Sept 2015

    trace('test pass')
