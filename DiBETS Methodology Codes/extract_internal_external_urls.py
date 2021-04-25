"""

This Code uses crawled html dump of all the homepages of supplied set of news websites' homepages and segregates output as internal/external urls.

All the extracted URLs from each website are separately stored (based on their type - internal/external) as a .txt file

"""

# Necessary Imports
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import os


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_short_domain(domain):
    '''
    Function to remove "www." and ".com" parts of a netloc
    '''
    start = end = 0
    for char in domain:
        if char == '.':
            start = domain.index(char) + 1
            break

    index = len(domain)
    for i in range(len(domain)):
        index -= 1
        if domain[index] == '.':
            end = index
            break

    return domain[start:end]


# Reading generated correct urls
input_urls_path = os.path.join(os.path.abspath(os.curdir),'websites_homepage_url.txt')
with open(input_urls_path, 'r', encoding='utf-8') as furl:
    Url_list = sorted(furl.read().split('\n'))
furl.close()

# Reading html dump
html_dump_path = os.path.join(os.path.abspath(os.curdir),'HTML Dump')
html_dump_filenames = [url_i.replace('https://','').replace('www.','').replace('.com/news','.txt').replace('.com/','.txt').replace('.org/','.txt') for url_i in Url_list]


# Output folder paths for storage of internal/ecternal link files. Keep this folders in the same folder that contains this script.
output_external_links_path = os.path.join(os.path.abspath(os.curdir),'External URLs')
output_internal_links_path = os.path.join(os.path.abspath(os.curdir),'Internal URLs')


for url in Url_list[:]:

    url_index = Url_list.index(url)
    print(url_index, url)
    domain_name = urlparse(url).netloc
    domain_name = get_short_domain(domain_name)
    
    internal_urls = set()
    external_urls = set()

    current_external_path = os.path.join(output_external_links_path, html_dump_filenames[url_index])
    current_internal_path = os.path.join(output_internal_links_path, html_dump_filenames[url_index])

    current_dump_path = os.path.join(html_dump_path, html_dump_filenames[url_index])

    # Reading the current dump and converting it to appropriate text format so that it can be applied string function "find_all()" to obtain hrefs
    with open(current_dump_path, 'r', encoding='utf-8') as fdump:
        text = fdump.read()
    fdump.close()
    soup = BeautifulSoup(text, 'html.parser')


    repeat_external_cnt = 0
    repeat_internal_cnt = 0

    for a_tag in soup.findAll("a"):

        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue

        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if not is_valid(href):
            continue
        if href in internal_urls:
            repeat_internal_cnt += 1
            continue
        if domain_name not in href:
            if href not in external_urls:
                external_urls.add(href)
            else:
                repeat_external_cnt += 1
            continue

        if href[len(href)-1] != "/":
            href = href + "/"

        internal_urls.add(href)

    external_urls = list(external_urls)
    internal_urls = list(internal_urls)
    unique_external_cnt = len(external_urls)
    unique_internal_cnt = len(internal_urls)
    print(repeat_internal_cnt, unique_internal_cnt, "|", repeat_external_cnt, unique_external_cnt)

    
    # Printing URLs which have either the internal link or external link count as 0
    if len(external_urls) == 0 or len(internal_urls) == 0:
        print(url_index-1, url, len(internal_urls), "|", len(external_urls))

    # Saving External Links of the current website to a separate file
    with open(current_external_path, 'w', encoding='utf-8') as fext:
        for link in external_urls:
            fext.write(link)
            if external_urls.index(link) != len(external_urls)-1:
                fext.write("\n")
    fext.close()

    # Saving Internal Links of the current website to a separate file
    with open(current_internal_path, 'w', encoding='utf-8') as fint:
        for link in internal_urls:
            fint.write(link)
            if internal_urls.index(link) != len(internal_urls)-1:
                fint.write("\n")
    fint.close()
