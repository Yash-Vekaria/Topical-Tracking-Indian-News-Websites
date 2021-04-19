import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import numpy as np
from urllib.parse import urlparse
# %matplotlib inline


def read_file(path, filename):
	f = open(os.path.join(path, filename), 'r')
	text = f.read()
	f.close()
	return text


# Plot Histogram on URL Filtering Parameters

import seaborn as sns
import os
sns.set_style("white")

url_lengths = []
subpath_lengths = []
hyphen_counts = []

top25 = ['aajtak.intoday.txt','jagran.txt','rvcj.txt','bhaskar.txt','zeenews.india.txt','indiatvnews.txt','timesofindia.indiatimes.txt','indiatoday.txt',
		 'news24online.txt','news.abplive.txt','bbc.txt','ndtv.txt','amarujala.txt','indiatimes.txt','navbharattimes.indiatimes.txt','indianexpress.txt',
		 'thequint.txt','patrika.txt','news18.txt','thelogicalindian.txt','hindustantimes.txt','timesnownews.txt','punjabkesari.txt','thehindu.txt',
		 'anandabazar.txt']

internal_links_path = os.path.join(os.path.abspath(os.curdir),'Internal URLs')
for file in os.listdir(internal_links_path)[:]:
	if file not in top25:
		continue
	text_il = read_file(internal_links_path, file)
	internal_links = text_il.split("\n")

	for link in internal_links:
		url_path = urlparse(link.lower()).path
		url_host = urlparse(link.lower()).netloc

		url_lengths.append(len(link))

		for w in url_path.strip('/').split('/'):
			subpath_lengths.append(len(w))
			hyphen_counts.append(w.count("-"))


kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2})

fig = plt.figure(figsize=(10,7), dpi= 80)
sns.distplot(url_lengths, bins=300, color="dodgerblue", label="Length(URL)", **kwargs)
sns.distplot(subpath_lengths, bins=300, color="orange", label="Length(subpath)", **kwargs)
sns.distplot(hyphen_counts, bins=300, color="deeppink", label="Count(\"-\", subpath)", **kwargs)

plt.xlim(0,150)
plt.ylim(0,0.11)
plt.legend()
plt.xlabel('Parameter Values')
plt.xticks(np.arange(0, 150, step=5))

# Positions of prameter thresholds to be shown with red vertical dotted lines
xposition = [4, 30, 80]
colors = ['deeppink', 'orange', 'dodgerblue']
xlabel = ['count(“-”,subpath) <= 3', 'length(subpath) <= 23', 'Length(URL) <= 65']
for x in range(len(xposition)):
    plt.axvline(x=xposition[x], ymin=0, ymax=1, color=colors[x], linestyle='--', label=xlabel[x])

fig.savefig("URLFilteringParams.pdf", bbox_inches='tight')
plt.show()

####################################################################################