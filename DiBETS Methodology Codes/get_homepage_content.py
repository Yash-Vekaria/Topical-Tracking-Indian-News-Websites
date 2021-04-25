"""

This Code crawls and generates a .txt of all the complete valid urls from its short version
For e.g. abc.com --> https://abc.com/

"""

# Necessary Imports
import requests
import pandas as pd
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import re
import os


def get_complete_url(url_test):
    """
    Checks whether a url with given scheme and domain provides content and exists or not
    """
    try:
        reqs = requests.get(url_test) 
        soup = BeautifulSoup(reqs.text, 'html.parser')
        print(len(str(soup)), type(soup)) 
    except Exception as e:
        print(e)
        return 'None', False, url_test
    return soup, True, url_test


# Url_list must contain urls with 'http', 'www.' and '.com' parts.

# Input path to the csv containing all the homepage URLS of Websites
input_urls_path = os.path.join(os.path.abspath(os.curdir),'websites_homepage_urls.txt')
with open(input_urls_path, 'r', encoding='utf-8') as furl:
    Url_list = sorted(furl.read().split('\n'))
furl.close()

# Ensure that the HTML Dump folder is created inside the same folder that contains this script
html_dump_path = os.path.join(os.path.abspath(os.curdir),'HTML Dump')
for urll in Url_list[:]:

    url_index = int(Url_list.index(urll))

    soup, valid, url = get_complete_url(urll)

    path = os.path.join(html_dump_path, url.replace('https://','').replace('www.','').replace('.com/news','.txt').replace('.com/','.txt').replace('.org/','.txt'))
    if soup == 'None' or not(valid):
        print(url_index, urll, "NOT FOUND!")
        continue
    else:
        fdump = open(path, 'w', encoding="utf-8")
        fdump.write(str(soup))
        fdump.close()
        print(url)
