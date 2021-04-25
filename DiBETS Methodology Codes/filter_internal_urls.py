"""

The internal URLs are analysed by plotting their distrinbution of the below mentioned parameters and derived cut-offs are used to filter the internal URLs.
This ensure that only section-type urls are retained for analysis (i.e. article urls are rejected).
1. length(url) <= 80
2. length(url_category) <= 30
3. count('-', url_category) <= 4

All the filtered internal URLs from each website are separately stored as a .txt file

"""

# Necessary imports
import os
from urllib.parse import urlparse

# Function to read a file
def read_file(path, filename):
	f = open(os.path.join(path, filename), 'r')
	text = f.read()
	f.close()
	return text


def write_filtered_urls(filtered_urls, path, filename):
	output_file_path = os.path.join(filtered_links_path, filename)
	with open(output_file_path, 'w', encoding='utf-8') as fout:
		for link in filtered_urls:
			fout.write(link)
			if filtered_urls.index(link) != len(filtered_urls)-1:
				fout.write("\n")
	fout.close()
	return

def filter_urls(internal_urls, path, filename):
	filtered_urls = []
	for link in internal_urls:
		url_path = urlparse(link.lower()).path
		url_host = urlparse(link.lower()).netloc

		if (len(link) <= 65) and (" " not in link) and (url_host not in url_path) and (len(url_path) >= 3):
			url_parts = [w for w in url_path.strip('/').split('/') if len(w) <= 23 and w.count("-") <= 3 and w != '']
			if len(url_parts) == len(url_path.strip('/').split('/')):
				filtered_urls.append(link)
	write_filtered_urls(filtered_urls, path, filename)
	return filtered_urls


#Input/Output folder paths fo storage of internal/filtered link files
filtered_links_path = os.path.join(os.path.abspath(os.curdir),'Filtered URLs')
internal_links_path = os.path.join(os.path.abspath(os.curdir),'Internal URLs')

cnt = 0
for file in os.listdir(internal_links_path)[:]:
	
	cnt += 1
	print(cnt, file)
	curr_il = curr_fl = 0
	
	internal_links = read_file(internal_links_path, file).split("\n")
	filtered_links = filter_urls(internal_links, filtered_links_path, file)
